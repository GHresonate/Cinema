# Generated by Django 4.0.6 on 2022-09-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='place',
            field=models.CharField(max_length=32),
        ),
    ]
