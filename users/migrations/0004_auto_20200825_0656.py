# Generated by Django 3.1 on 2020-08-25 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_debt_grps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='debt',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='debt_grps',
        ),
    ]