# Generated by Django 4.0.6 on 2022-08-14 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0005_alter_seo_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsAndDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('News', 'News'), ('Discount', 'Discount')], max_length=16)),
                ('date_published', models.DateField()),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=256)),
                ('main_photo', models.ImageField(upload_to='')),
                ('url', models.URLField()),
                ('photo_list', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages_app.gallery')),
            ],
        ),
        migrations.AlterField(
            model_name='newsanddiscinbanner',
            name='type',
            field=models.CharField(choices=[('News', 'News'), ('Discount', 'Discount')], max_length=16),
        ),
        migrations.AlterField(
            model_name='seo',
            name='url',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.DeleteModel(
            name='NewsAndDiscont',
        ),
        migrations.AddField(
            model_name='newsanddiscount',
            name='seo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages_app.seo'),
        ),
    ]
