# Generated by Django 4.0.6 on 2022-08-26 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0027_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='phone_number',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='phone_number2',
            field=models.CharField(max_length=64),
        ),
    ]
