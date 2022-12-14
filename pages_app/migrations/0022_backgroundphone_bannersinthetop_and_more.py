# Generated by Django 4.0.6 on 2022-08-21 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0021_alter_newsanddiscount_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_photo', models.ImageField(upload_to='')),
                ('type', models.CharField(choices=[('Photo', 'Photo'), ('Phone', 'Phone')], max_length=16, null=True)),
                ('color', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='BannersInTheTop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_photo', models.ImageField(upload_to='')),
                ('text', models.TextField()),
                ('url', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='newsanddiscinbanner',
            name='page',
        ),
        migrations.RemoveField(
            model_name='newsanddiscinbanner',
            name='text',
        ),
        migrations.RemoveField(
            model_name='newsanddiscinbanner',
            name='type',
        ),
        migrations.AlterField(
            model_name='newsanddiscinbanner',
            name='trailer_url',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Banners',
        ),
    ]
