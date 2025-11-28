from django.contrib import admin

from post.models import Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author')


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'author')
