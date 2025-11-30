from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
    )
    content = models.TextField(
        verbose_name="Текст",
    )
    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True,
        verbose_name="Изображение",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='posts',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Commentary(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='commentaries',
    )
    content = models.TextField(
        verbose_name="Текст",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост',
        related_name='commentaries',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.content} от {self.author}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"



