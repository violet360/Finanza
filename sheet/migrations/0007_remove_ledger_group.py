# Generated by Django 3.1 on 2020-08-24 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0006_auto_20200824_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledger',
            name='group',
        ),
    ]