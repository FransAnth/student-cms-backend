# Generated by Django 4.2.6 on 2024-08-03 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_studentschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentschedule',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
