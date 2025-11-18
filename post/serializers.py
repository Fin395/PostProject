from rest_framework import serializers

from post.models import Commentary, Post


class CommentarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Commentary
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"
