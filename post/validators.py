from rest_framework import serializers


class PostTitleValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_title = dict(value).get(self.field)
        forbidden_words = ["ерунд", "глупост", "чепух"]
        result = []

        if tmp_title:
            title_words = tmp_title.split()

            for forbidden_word in forbidden_words:
                result.append(any(forbidden_word in word for word in title_words))
            if True in result:
                raise serializers.ValidationError(
                    "The title must not contain the words: ерунда, глупость, чепуха"
                )
