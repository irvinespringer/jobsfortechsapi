# Generated by Django 2.1.1 on 2019-02-06 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_candidate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='location',
            new_name='company_location',
        ),
    ]
