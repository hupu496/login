# Generated by Django 3.0.1 on 2020-01-15 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0015_auto_20200114_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp',
            name='user',
        ),
        migrations.AddField(
            model_name='otp',
            name='auth_user',
            field=models.OneToOneField(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
