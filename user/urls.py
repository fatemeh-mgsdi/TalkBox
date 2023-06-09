from django.urls import path

from user.views import UserRegisterView, LoginRegisterView, UserList


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", LoginRegisterView.as_view(), name="login"),
    path('', UserList.as_view(), name='user-list'),
]
