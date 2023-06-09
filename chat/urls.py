from django.urls import path, include


from rest_framework import routers
from .views import ChatRoomViewSet, ChatMessageViewSet

router = routers.DefaultRouter()
router.register(r"rooms", ChatRoomViewSet)
router.register(r"messages", ChatMessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
