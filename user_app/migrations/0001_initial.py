# Generated by Django 4.0.6 on 2022-07-29 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinema_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
                ('nickname', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('language', models.CharField(choices=[('UA', 'Ukrainian'), ('EN', 'English'), ('RU', 'Russian')], max_length=2)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Different', 'Different'), ('Don`t say', 'Don`t say')], max_length=32)),
                ('phone_number', models.IntegerField()),
                ('birthday', models.DateField()),
                ('city', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.session')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_app.user')),
            ],
        ),
    ]
