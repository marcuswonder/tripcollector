# Generated by Django 4.1.6 on 2023-02-10 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_rename_duration_segment_duration_hrs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='region',
        ),
    ]