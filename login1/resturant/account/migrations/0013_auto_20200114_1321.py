# Generated by Django 3.0.1 on 2020-01-14 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0012_auto_20200114_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='username',
            field=models.OneToOneField(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
