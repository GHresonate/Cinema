# Generated by Django 4.0.6 on 2022-09-10 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0016_session_time_alter_session_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='time',
            field=models.TimeField(),
        ),
    ]