# Generated by Django 5.0.7 on 2025-03-02 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0006_alter_classroom_options_alter_classschedule_options_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='classroom',
            table='classrooms',
        ),
        migrations.AlterModelTable(
            name='classschedule',
            table='classroom_scheds',
        ),
    ]
