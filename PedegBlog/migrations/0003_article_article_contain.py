# Generated by Django 2.1.4 on 2019-03-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PedegBlog', '0002_remove_usercount_view_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_contain',
            field=models.TextField(blank=True, null=True),
        ),
    ]
