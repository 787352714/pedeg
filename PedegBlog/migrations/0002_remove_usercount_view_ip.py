# Generated by Django 2.1.4 on 2019-03-18 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PedegBlog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercount',
            name='view_ip',
        ),
    ]