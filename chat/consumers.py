import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from rest_framework.authtoken.models import Token

from .models import ChatRoom, ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def get_user(self, token):
        User = get_user_model()
        try:
            token_key = token
            token = await database_sync_to_async(Token.objects.get)(key=token_key)
            return await database_sync_to_async(User.objects.get)(pk=token.user_id)
        except (Token.DoesNotExist, User.DoesNotExist):
            return None

    async def connect(self):
        self.token = self.scope["query_string"].decode("utf-8").split("=")[1]
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        user = await self.get_user(self.token)

        if not user.is_authenticated:
            await self.close()

        self.scope["user"] = user

        try:
            self.chat_room = await database_sync_to_async(ChatRoom.objects.get)(
                id=self.room_name
            )

        except ChatRoom.DoesNotExist:
            await self.close()

        if user not in await database_sync_to_async(list)(self.chat_room.members.all()):
            await self.close()
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        sender = self.scope["user"]

        # Save message to database
        chat_message = await database_sync_to_async(ChatMessage.objects.create)(
            room=self.chat_room, sender=sender, message=text_data
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": text_data,
                "sender": sender.username,
                "created_at": chat_message.created_at.isoformat(),
            },
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]
        created_at = event["created_at"]

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "sender": sender,
                    "created_at": created_at,
                }
            )
        )
