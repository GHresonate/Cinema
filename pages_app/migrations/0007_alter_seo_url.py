# Generated by Django 4.0.6 on 2022-08-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0006_newsanddiscount_alter_newsanddiscinbanner_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='url',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
    ]
