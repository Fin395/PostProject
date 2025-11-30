from rest_framework import serializers
from datetime import datetime, date


class PostTitleValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_title = dict(value).get(self.field)
        forbidden_words = ['ерунд', 'глупост', 'чепух']
        title_words = tmp_title.split()
        result = []

        for forbidden_word in forbidden_words:
            result.append(any(forbidden_word in word for word in title_words))
        if True in result:
            raise serializers.ValidationError('The title must not contain the words: ерунда, глупость, чепуха')





# class PostAuthorAgeValidator:
#
#     def __init__(self, field):
#         self.field = field
#
#     def __call__(self, value):
#         tmp_value = dict(value).get(self.field)
#         birthday = datetime.strptime(str(tmp_value), '%d/%m/%Y')
#         today = date.today()
#         age = (today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day)))
#
#         if age < 18:
#             raise serializers.ValidationError('The author must be over 18 years old')


# from datetime import datetime, date
#
# today = date.today()
# # datetime.now())
# birthday = date(2005, 12, 1)
#
# (print
#  (today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))))
