from rest_framework import serializers

from users.models import User
from users.validators import (EmailValidator, PasswordDigitsValidator,
                              PasswordLengthValidator)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True, "required": True}}
        validators = [
            EmailValidator(field="email"),
            PasswordLengthValidator(field="password"),
            PasswordDigitsValidator(field="password"),
        ]


class UserReducedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "is_staff"]
        validators = [
            EmailValidator(field="email"),
            PasswordLengthValidator(field="password"),
            PasswordDigitsValidator(field="password"),
        ]
