# Generated by Django 5.0.6 on 2024-08-16 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbankaccount',
            old_name='account_number',
            new_name='account_no',
        ),
    ]