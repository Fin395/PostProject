from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from rest_framework.permissions import AllowAny

from users.views import UserCreateAPIView, UserRetrieveAPIView, UserListAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

# router = DefaultRouter()
# router.register(r"users", UserViewSet, basename="users")

urlpatterns = ([
    path("user/register/", UserCreateAPIView.as_view(), name="user-register"),
    path("user/update/<int:pk>/", UserUpdateAPIView.as_view(), name="user-update"),
    path("user/<int:pk>/", UserRetrieveAPIView.as_view(), name="user-get"),
    path(
        "token/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("users/", UserListAPIView.as_view(), name="user-list"),
    path("user/delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user-delete"),
])
# + router.urls)
