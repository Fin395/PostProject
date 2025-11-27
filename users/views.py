from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()





# class UserViewSet(ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
#     def get_permissions(self):
#         self.permission_classes = []
#
#         if self.action == 'create':
#             self.permission_classes = [AllowAny]
#
#         return super().get_permissions()