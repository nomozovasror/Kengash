# Generated by Django 5.1.4 on 2025-02-24 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0009_selectedemployee_status_selectedemployee_voted'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectedemployee',
            name='is_running',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='selectedemployee',
            name='timer_seconds',
            field=models.IntegerField(default=0),
        ),
    ]
