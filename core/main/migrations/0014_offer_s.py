# Generated by Django 5.0.4 on 2024-04-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_offer_but_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer_s',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='offer/', verbose_name='Offer image')),
                ('name', models.CharField(max_length=250, verbose_name='Upto')),
            ],
        ),
    ]