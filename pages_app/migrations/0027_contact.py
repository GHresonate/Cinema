# Generated by Django 4.0.6 on 2022-08-25 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0026_mainpage_phone_number_mainpage_phone_number2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.TextField()),
                ('coordinate', models.CharField(max_length=256)),
                ('main_photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
