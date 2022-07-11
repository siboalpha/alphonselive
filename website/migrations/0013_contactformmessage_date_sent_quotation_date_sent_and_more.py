# Generated by Django 4.0.4 on 2022-07-11 17:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_remove_specialofferleads_industry'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactformmessage',
            name='date_sent',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='quotation',
            name='date_sent',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='specialofferleads',
            name='date_sent',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
