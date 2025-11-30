from rest_framework import serializers

from post.models import Commentary, Post
from post.validators import PostTitleValidator
from users.serializers import UserReducedSerializer


class CommentarySerializer(serializers.ModelSerializer):
    author = UserReducedSerializer(read_only=True)

    class Meta:
        model = Commentary
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    commentaries = CommentarySerializer(many=True, read_only=True)
    author = UserReducedSerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        validators = [PostTitleValidator(field="title")]
