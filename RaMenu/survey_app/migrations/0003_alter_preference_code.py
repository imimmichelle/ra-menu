# Generated by Django 4.2.4 on 2024-01-26 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0002_rename_sequence_preference_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='code',
            field=models.CharField(max_length=256),
        ),
    ]