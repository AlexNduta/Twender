from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    
    list_display = ['username', 'email', 'is_staff', 'is_conductor']
    fieldsets = UserAdmin.fieldsets +(
            (None, {'fields': ('is_conductor',)}),
            )
    add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {'fields': ('is_conductor',)}),
            )
    
admin.site.register(User, CustomUserAdmin)
