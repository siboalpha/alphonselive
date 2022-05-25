# Generated by Django 4.0.4 on 2022-05-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_contactformmessages_contactformmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=40)),
                ('website_type', models.CharField(choices=[('Basic Website', 'Web design'), ('Standard Website', 'Standard Website'), ('Advanced Website', 'Advanced Website')], default='Basic Website', max_length=40)),
                ('domain_name', models.BooleanField(default=False)),
                ('hosting', models.BooleanField(default=False)),
                ('web_design', models.BooleanField(default=False)),
                ('web_development', models.BooleanField(default=False)),
                ('technical_suport', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='specialOfferLeads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('phone_number', models.CharField(max_length=40)),
                ('industry', models.CharField(max_length=40)),
                ('website_details', models.TextField(max_length=500)),
            ],
        ),
    ]
