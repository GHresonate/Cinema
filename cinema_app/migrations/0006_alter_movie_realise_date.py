# Generated by Django 4.0.6 on 2022-08-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0005_alter_movie_realise_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='realise_date',
            field=models.DateField(),
        ),
    ]