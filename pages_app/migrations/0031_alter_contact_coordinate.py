# Generated by Django 4.0.6 on 2022-09-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0030_rename_description_seo_definition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='coordinate',
            field=models.TextField(),
        ),
    ]