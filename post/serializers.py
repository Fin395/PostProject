from rest_framework import serializers

from post.models import Commentary, Post
from post.validators import PostTitleValidator


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        validators = [PostTitleValidator(field='title')]
