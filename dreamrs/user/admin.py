from django.contrib import admin


# Register your models here.
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin

from . import models

class ProfileAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('images_view',)
    list_display_links = UserAdmin.list_display_links + ('username', 'email')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('photo', 'adresse', 'website', 'description')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('photo', 'adresse', 'website', 'description')}),
    )

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="height:60px; width:60px">')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)