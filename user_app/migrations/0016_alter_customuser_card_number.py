# Generated by Django 4.1.1 on 2022-09-14 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0015_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='card_number',
            field=models.CharField(max_length=256, null=True),
        ),
    ]