from django.contrib import admin
from accounts.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'is_admin',
        'is_superadmin',
        'data_joined',
        'is_active',
    )
    list_display_links = list_display
    readonly_fields = ('last_login', 'password')
    ordering = ('-data_joined',)
    fieldsets = ()
    filter_horizontal = ()
    list_filter = ()
