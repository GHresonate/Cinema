# Generated by Django 4.0.6 on 2022-08-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0015_alter_newsanddiscount_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsanddiscount',
            name='type',
            field=models.CharField(choices=[('News', 'News'), ('Discount', 'Discount')], max_length=16, null=True),
        ),
    ]