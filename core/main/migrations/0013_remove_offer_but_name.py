# Generated by Django 5.0.4 on 2024-04-30 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_blog_name1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='but_name',
        ),
    ]