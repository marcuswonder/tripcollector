# Generated by Django 4.1.6 on 2023-02-08 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_rename_visit_trip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='country',
        ),
        migrations.AddField(
            model_name='trip',
            name='countries',
            field=models.ManyToManyField(to='main_app.country'),
        ),
    ]
