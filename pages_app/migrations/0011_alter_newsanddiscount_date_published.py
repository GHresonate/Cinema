# Generated by Django 4.0.6 on 2022-08-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0010_alter_newsanddiscount_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsanddiscount',
            name='date_published',
            field=models.DateField(default=0),
        ),
    ]
