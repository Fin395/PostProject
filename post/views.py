from datetime import date

from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from post.models import Commentary, Post
from post.serializers import CommentarySerializer, PostSerializer
from users.permissions import IsOwnerOrAdmin


class CommentaryViewSet(ModelViewSet):
    serializer_class = CommentarySerializer
    queryset = Commentary.objects.all()

    def get_permissions(self):
        self.permission_classes = []

        if self.action == "create":
            self.permission_classes = [IsAuthenticated]

        elif self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.validated_data["author"] = self.request.user
        serializer.save()


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_permissions(self):
        self.permission_classes = []

        if self.action == "create":
            self.permission_classes = [IsAuthenticated]

        elif self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        user = self.request.user
        today = date.today()

        age = (
            today.year
            - user.birth_date.year
            - ((today.month, today.day) < (user.birth_date.month, user.birth_date.day))
        )

        if age < 18:
            raise serializers.ValidationError(
                "The post author must be over 18 years old"
            )

        serializer.validated_data["author"] = user
        serializer.save()
