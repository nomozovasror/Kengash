# Generated by Django 5.1.4 on 2024-12-06 19:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_candidatesvotes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatesvotes',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voter_teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]
