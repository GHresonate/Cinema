# Generated by Django 4.0.6 on 2022-07-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='created_date',
            field=models.DateField(),
        ),
    ]
