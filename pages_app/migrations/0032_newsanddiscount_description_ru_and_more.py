# Generated by Django 4.0.6 on 2022-09-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0031_alter_contact_coordinate'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsanddiscount',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='newsanddiscount',
            name='description_uk',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='newsanddiscount',
            name='name_ru',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='newsanddiscount',
            name='name_uk',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='newsanddiscount',
            name='trailer_url_ru',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='newsanddiscount',
            name='trailer_url_uk',
            field=models.URLField(null=True),
        ),
    ]
