# Generated by Django 4.0.4 on 2022-09-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_remove_specialofferleads_whatsapp_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='freewebsitelead',
            name='status',
            field=models.CharField(choices=[('Contacted', 'Contacted'), ('Not contacted', 'Not contacted'), ('Not paid', 'Not paid'), ('Payment_pending', 'Payment_pending')], default='Not contacted', max_length=255, null=True),
        ),
    ]
