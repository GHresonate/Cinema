# Generated by Django 4.0.6 on 2022-09-04 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0011_rename_definition_movie_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hall',
            name='created_date',
        ),
    ]
