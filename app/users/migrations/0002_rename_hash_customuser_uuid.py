# Generated by Django 5.1.4 on 2024-12-06 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='hash',
            new_name='uuid',
        ),
    ]
