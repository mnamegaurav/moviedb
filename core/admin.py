from django.contrib import admin

from core.models import Movie, Comment
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    model = Movie


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
