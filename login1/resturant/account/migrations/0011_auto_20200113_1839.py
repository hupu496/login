# Generated by Django 3.0.1 on 2020-01-13 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200113_1823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otp',
            old_name='user_id',
            new_name='user',
        ),
    ]
