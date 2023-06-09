from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import ChatRoom, ChatMessage


class ChatRoomSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    class Meta:
        model = ChatRoom
        fields = ["id", "name", "members"]

    def get_members(self, obj):
        member_ids = obj.members.all()
        members = get_user_model().objects.filter(id__in=member_ids)
        return members.values("id", "username")


class ChatMessageSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField()

    class Meta:
        model = ChatMessage
        fields = "__all__"

    def get_sender(self, obj):
        sender_id = obj.sender.id
        sender = get_user_model().objects.get(id=sender_id)
        return {"id": sender.id, "username": sender.username}
