# Generated by Django 5.1.4 on 2025-02-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0007_alter_selectedemployee_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotingTimer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seconds', models.IntegerField(default=0)),
                ('is_running', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Voting Timer',
                'verbose_name_plural': 'Voting Timers',
            },
        ),
    ]
