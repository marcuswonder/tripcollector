# Generated by Django 4.1.6 on 2023-02-08 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='title',
            field=models.CharField(default='Demo', max_length=100),
            preserve_default=False,
        ),
    ]
