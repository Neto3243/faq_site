from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'date_of_birth')
    list_filter = ('status', 'user')
