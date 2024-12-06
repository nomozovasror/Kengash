from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomUser(AbstractUser):
    hemis_id = models.CharField(max_length=200, null=True)
    id_number = models.CharField(max_length=200, null=True, unique=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    picture = models.CharField(max_length=300, null=True)
    short_name = models.CharField(max_length=300, null=True)
    full_name = models.CharField(max_length=300, null=True)
    third_name = models.CharField(max_length=300, null=True)
    phone = models.CharField(max_length=300, null=True)
    roles = models.JSONField(null=True)
    active_role = models.CharField(max_length=300, null=True)
    uuid = models.CharField(max_length=300, null=True, blank=True)
    voted = models.BooleanField(default=False)
