# Generated by Django 3.1.2 on 2020-11-19 23:13

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataverses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manifesttestparams',
            name='raw_file',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/code/server/test_setup/user_uploaded_data'), upload_to='mock-files/%Y/%m/%d/'),
        ),
    ]
