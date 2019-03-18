from django.db import models

# Create your models here.
class UserCount(models.Model):
    view_id = models.AutoField
    view_ip = models.IPAddressField
    view_date = models.DateTimeField('view time')

class Article(models.Model):
    article_id = models.AutoField
    article_header = models.CharField(max_length=200)
    article_contain = models.TextField(blank=True, null=True)
    article_time = models.DateTimeField('pub time')

class ShortArtical(models.Model):
    shortartical_id = models.AutoField
    shortartical_contain = models.CharField(max_length=500)
    shortartical_time = models.DateTimeField('shortpub time')