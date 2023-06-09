from rest_framework import viewsets
from rest_framework.response import Response
from .models import ChatRoom, ChatMessage
from .serializers import ChatRoomSerializer, ChatMessageSerializer
from rest_framework.permissions import IsAuthenticated


class ChatRoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatRoomSerializer
    queryset = ChatRoom.objects.all()

    def retrieve(self, request, pk=None):
        chatroom = ChatRoom.objects.get(id=pk)
        serializer = ChatRoomSerializer(chatroom)
        return Response(serializer.data)



class ChatMessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatMessageSerializer
    queryset = ChatMessage.objects.order_by("created_at")
    
    def get_queryset(self):
        room_id = self.request.query_params.get("room_id")
        if room_id is not None:
            return ChatMessage.objects.filter(room__id=room_id).order_by("created_at")
        else:
            return self.queryset