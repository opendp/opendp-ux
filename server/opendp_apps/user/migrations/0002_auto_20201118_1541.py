# Generated by Django 3.1.2 on 2020-11-18 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataverseuser',
            old_name='dataverse_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='dataverseuser',
            old_name='dataverse_first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='dataverseuser',
            old_name='dataverse_last_name',
            new_name='last_name',
        ),
    ]
