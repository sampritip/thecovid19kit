# Generated by Django 3.2 on 2021-05-08 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20210509_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post2',
            name='ageofp',
        ),
    ]
