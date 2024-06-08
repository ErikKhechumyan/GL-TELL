# Generated by Django 5.0.4 on 2024-04-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='client/', verbose_name='Client image')),
                ('name', models.CharField(max_length=250, verbose_name='Client name')),
                ('text', models.TextField(verbose_name='Client text')),
            ],
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Hndik name')),
                ('name1', models.CharField(max_length=250, verbose_name='Hndik name')),
                ('img', models.ImageField(upload_to='hndik/', verbose_name='Hndik image')),
                ('text', models.TextField(verbose_name='Hndik text')),
            ],
        ),
        migrations.DeleteModel(
            name='hndik',
        ),
    ]