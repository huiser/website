from django.contrib import admin
from users.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'date_joined', 'date_left', ),
        }),
        ('Communication', {
            'classes': ('collapse',),
            'fields': (('mobile_phone', 'publish_mobile_phone', ), ('home_phone', 'publish_home_phone')),
        }),
        ('Security', {
            'classes': ('collapse',),
            'fields': ('ssh_public_key', ),
        }),
    )
    #fields = ['last_name', 'first_name', 'is_active', 'is_staff', 'date_joined', 'date_left', 'mobile', 'mobile_public', 'ssh_public_key', ]
    readonly_fields = ('date_joined',)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff',)
    list_display_links = ('username',)
    list_filter = ('is_staff', 'is_active', )
    ordering = ('last_name', 'first_name' )
    search = ('username', 'email', 'last_name', 'first_name', 'mobile', )


admin.site.register(CustomUser, CustomUserAdmin)
