# Generated by Django 5.1.3 on 2024-11-18 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='row',
            name='content',
            field=models.JSONField(default=list),
        ),
    ]
