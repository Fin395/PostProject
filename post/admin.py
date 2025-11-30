from django.contrib import admin

from post.models import Commentary, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "author", "author__birth_date")
    list_filter = ("created_at",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "author")
