from django.contrib import admin
from .models import Article
from .models import ShortArtical

# Register your models here.
admin.site.register(Article)
admin.site.register(ShortArtical)