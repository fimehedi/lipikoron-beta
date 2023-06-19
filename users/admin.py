from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group as Default_Group
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from import_export.admin import ImportExportModelAdmin


from .models import CustomUser, Withdraw, Notification, Group


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


class withdrawModel(ImportExportModelAdmin):
    list_display = ["__str__"]
    list_per_page = 25
    search_fields = ["__str__"]
    list_filter = ['payment_done',]
    class Meta:
        Model = Withdraw
admin.site.register(Withdraw, withdrawModel)

admin.site.register(Notification)

admin.site.unregister(Default_Group)
admin.site.register(Group)