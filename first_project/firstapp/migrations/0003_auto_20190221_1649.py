# Generated by Django 2.1.7 on 2019-02-21 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_accessrecords'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccessRecords',
            new_name='AccessRecord',
        ),
    ]