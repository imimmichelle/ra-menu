# Generated by Django 4.2.4 on 2024-01-19 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preference',
            old_name='sequence',
            new_name='code',
        ),
    ]
