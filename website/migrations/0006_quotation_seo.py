# Generated by Django 4.0.4 on 2022-05-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_quotation_quotation_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='seo',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=40),
        ),
    ]
