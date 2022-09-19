# Generated by Django 4.1.1 on 2022-09-19 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0018_alter_session_hall'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cinema',
            name='description_uk',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cinema',
            name='name_ru',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='cinema',
            name='name_uk',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
