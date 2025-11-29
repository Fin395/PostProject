from rest_framework import serializers


class EmailValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        domain = tmp_value.split('@')[-1]
        if domain not in ['mail.ru', 'yandex.ru']:
            raise serializers.ValidationError('Only mail.ru or yandex.ru domains are acceptable')


class PasswordLengthValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)

        if len(tmp_value) < 8:
            raise serializers.ValidationError('The password must consist of at least 8 symbols')

        # elif not any(symbol.isdigit() for symbol in tmp_value):
        #     raise serializers.ValidationError('The password must contain at least one digit')


class PasswordDigitsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)

        # if len(tmp_value) < 8:
        #     raise serializers.ValidationError('The password must consist of at least 8 symbols')

        if not any(symbol.isdigit() for symbol in tmp_value):
            raise serializers.ValidationError('The password must contain at least one digit')
