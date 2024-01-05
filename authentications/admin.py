from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group


class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'is_staff')
    fieldsets = (
        ('ユーザー情報', {
            'fields': (
                'username', 'email', 'password'
            )
        }),
        ('パーミッション', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser'
            )
        }),
    )

    add_fieldsets = (
        ('ユーザー情報', {
            'fields': (
                'username','email', 'password', 'confirm_password'
            )
        }),
    )

    list_filter = ('is_staff', 'is_superuser', 'is_active',)

    search_fields = ('email', 'username',)


admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.unregister(Group) 