from django.contrib import admin
from .models import Article
from .models import ShortArtical

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'article_header', 'article_contain', 'article_time']

class ShortArticalAdmin(admin.ModelAdmin):
    list_display = ['id', 'shortartical_contain', 'shortartical_time']


admin.site.register(Article, ArticleAdmin)
admin.site.register(ShortArtical, ShortArticalAdmin)