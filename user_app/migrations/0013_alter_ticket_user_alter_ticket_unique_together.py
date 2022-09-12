# Generated by Django 4.0.6 on 2022-09-12 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0017_alter_session_time'),
        ('user_app', '0012_alter_ticket_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='ticket',
            unique_together={('session', 'place', 'row')},
        ),
    ]
