# Generated by Django 2.2.17 on 2021-01-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190227_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_service_account',
            field=models.BooleanField(default=False),
        ),
    ]