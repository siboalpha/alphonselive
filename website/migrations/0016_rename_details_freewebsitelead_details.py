# Generated by Django 4.0.4 on 2022-08-15 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_rename_freewebsirelead_freewebsitelead'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freewebsitelead',
            old_name='Details',
            new_name='details',
        ),
    ]