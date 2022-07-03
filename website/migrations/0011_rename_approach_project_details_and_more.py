# Generated by Django 4.0.4 on 2022-07-03 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_remove_project_details_project_approach_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='approach',
            new_name='details',
        ),
        migrations.RemoveField(
            model_name='project',
            name='challenge',
        ),
        migrations.RemoveField(
            model_name='project',
            name='introduction',
        ),
        migrations.RemoveField(
            model_name='project',
            name='solution',
        ),
    ]
