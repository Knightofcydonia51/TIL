from django.contrib import admin
from .models import Article

class ArticelAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'content', 'created_at', 'updated_at')
    list_display_links=('content',)
    list_filter=('created_at',)
    list_editable=('title',)
    list_per_page=4

admin.site.register(Article,ArticelAdmin)