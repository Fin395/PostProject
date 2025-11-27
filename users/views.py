from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsAdmin
from users.serializers import UserSerializer, UserReducedSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


# class UserUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     permission_classes = [IsAuthenticated, IsProfileOwner]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserReducedSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_serializer_class(self):
        if self.request.user == self.get_object():
            return UserSerializer
        return UserReducedSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserReducedSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]


# class UserDestroyAPIView(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     permission_classes = [IsAuthenticated]

