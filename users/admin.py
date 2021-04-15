from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
# from .forms import CustomUserCreationForm, CustomUserChangeForm

from import_export.admin import ImportExportModelAdmin



class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):
    list_display    = ['username', 'first_name',  'last_name', 'is_lipikar']
    list_editable   = ['is_lipikar']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
                )}
        ),
    )

    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': (
                'details',
                'profile_picture',
                'is_lipikar',
                'balance',
                'verified',
                )}
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)