# Generated by Django 4.0.6 on 2022-08-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0002_alter_seo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
