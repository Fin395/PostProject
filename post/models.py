from django.db import models

from users.models import User


class Commentary(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='Автор',
        blank=True,
        null=True,
        related_name='commentaries',
    )
    content = models.TextField(
        verbose_name="Текст",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Комментарий от {self.author}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


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
        on_delete=models.SET_NULL,
        verbose_name='Автор',
        blank=True,
        null=True,
        related_name='posts'
    )
    commentary = models.ManyToManyField(
        Commentary,
        verbose_name='Комментарии',
        related_name='posts',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
