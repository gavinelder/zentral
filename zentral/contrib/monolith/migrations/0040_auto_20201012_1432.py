# Generated by Django 2.2.15 on 2020-10-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monolith', '0039_auto_20201012_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolledmachine',
            name='serial_number',
            field=models.TextField(),
        ),
        migrations.AlterUniqueTogether(
            name='enrolledmachine',
            unique_together={('enrollment', 'serial_number')},
        ),
    ]
