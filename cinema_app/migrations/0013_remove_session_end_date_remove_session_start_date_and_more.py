# Generated by Django 4.0.6 on 2022-09-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0012_remove_hall_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='session',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='session',
            name='time',
        ),
        migrations.AddField(
            model_name='session',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
