# Generated by Django 4.0.6 on 2022-07-31 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
