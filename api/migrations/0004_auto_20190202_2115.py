# Generated by Django 2.1.1 on 2019-02-02 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190202_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='first_name',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='last_name',
            new_name='job_title',
        ),
    ]