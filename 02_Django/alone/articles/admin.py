from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display=('pk','title','content','created_at','updated_at',)

admin.site.register(Article, ArticleAdmin)







# from .models import Article

# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)

# admin.site.register(Article,ArticleAdmin)

