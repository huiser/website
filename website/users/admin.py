from django.contrib import admin
from users.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    fields = ['last_name', 'first_name', 'is_active', 'is_staff', 'date_joined', 'date_left', 'mobile', 'mobile_public', 'ssh_public_key', ]
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff',]
    list_display_links = ['username',]
    ordering = ['last_name', 'first_name' ]
    search = ['username', 'email', 'last_name', 'first_name', 'mobile', ]


admin.site.register(CustomUser, CustomUserAdmin)
