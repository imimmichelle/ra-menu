# Generated by Django 4.2.4 on 2024-03-03 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desire_app', '0002_alter_category_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desire',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='desire_app.category'),
        ),
    ]
