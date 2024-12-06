from django.contrib import admin
from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'username']
    list_display = ('full_name', 'username',  'roles',)
    list_display_links = ('full_name',)
    list_per_page = 25


admin.site.register(CustomUser, CustomUserAdmin)