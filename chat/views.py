from rest_framework import viewsets
from .models import ChatRoom, ChatMessage
from .serializers import ChatRoomSerializer, ChatMessageSerializer
from rest_framework.permissions import IsAuthenticated


class ChatRoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatRoomSerializer
    queryset = ChatRoom.objects.all()


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