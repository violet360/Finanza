# Generated by Django 3.1 on 2020-08-24 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0004_auto_20200824_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='group',
            field=models.CharField(max_length=100),
        ),
    ]