from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    fields=['title', 'content']

admin.site.register(Article,ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    fields = ['title', 'content']

admin.site.register(Comment,CommentAdmin)