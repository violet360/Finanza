# Generated by Django 3.1 on 2020-08-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger',
            name='group',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
