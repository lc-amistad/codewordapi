# Generated by Django 4.0.2 on 2022-02-21 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantes',
            name='restaurant_image',
            field=models.ImageField(default=1, upload_to='', verbose_name='view'),
            preserve_default=False,
        ),
    ]
