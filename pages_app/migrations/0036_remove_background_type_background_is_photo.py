# Generated by Django 4.1.1 on 2022-09-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0035_pages_description_ru_pages_description_uk_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='background',
            name='type',
        ),
        migrations.AddField(
            model_name='background',
            name='is_photo',
            field=models.BooleanField(default=True),
        ),
    ]
