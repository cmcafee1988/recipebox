# Generated by Django 3.1 on 2020-08-13 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Recipe',
        ),
    ]