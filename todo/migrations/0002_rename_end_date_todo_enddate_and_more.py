# Generated by Django 5.2.4 on 2025-07-30 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='end_date',
            new_name='enddate',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='start_date',
            new_name='startdate',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='Task',
            new_name='taskname',
        ),
    ]
