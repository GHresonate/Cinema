# Generated by Django 4.1.1 on 2022-09-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0036_remove_background_type_background_is_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
