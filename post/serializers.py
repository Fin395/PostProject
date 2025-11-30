from rest_framework import serializers

from post.models import Commentary, Post
from post.validators import PostTitleValidator


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = '__all__'
        extra_kwargs = {'author': {'read_only': True}}


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {'author': {'read_only': True}, 'commentary': {'many': True}}

        validators = [PostTitleValidator(field='title')]
