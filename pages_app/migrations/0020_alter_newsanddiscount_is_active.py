# Generated by Django 4.0.6 on 2022-08-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0019_rename_url_newsanddiscount_trailer_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsanddiscount',
            name='is_active',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]