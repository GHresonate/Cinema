# Generated by Django 4.0.6 on 2022-08-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0008_newsanddiscinbanner_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsanddiscinbanner',
            name='is_active',
        ),
        migrations.AddField(
            model_name='newsanddiscount',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
