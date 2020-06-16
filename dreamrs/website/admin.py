from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin

from . import models
from actions.action import Action



class SocialAccountAdmin(Action):
    list_display = ('nom', 'lien', 'date_add',
                    'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['lien']
    ordering = ['nom']

    fieldsets = [
        ('Info SocialAccount', {'fields': ['nom', 'lien', 'icon']}),
        ('Standare', {'fields': ['status']})
    ]



class SiteInfoAdmin(Action):
    list_display = ('icon_view', 'name', 'email', 'phone',
                    'date_add', 'date_update', 'status')
    search_fields = ('email', )
    date_hierarchy = 'date_add'
    list_display_links = ['name', 'email']
    ordering = ['name', 'email']
    
    fieldsets = [
        ('Info du site', {'fields': ['name', 'email', 'icon', 'description', 'phone', 'adresse']}),
        ('Standare', {'fields': ['status']})
    ]

    def icon_view(self, obj):
        return mark_safe(f'<img src="{obj.icon.url}" style="height:50px; width:50px">')



class NewsLetterAdmin(Action):
    list_display = ('email', 'date_add', 'date_update', 'status')
    search_fields = ('email', )
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    ordering = ['email']
    
    fieldsets = [
        ('Info NewsLetter', {'fields': ['email']}),
        ('Standare', {'fields': ['status']})
    ]



class ContactAdmin(Action):
    list_display = ('nom', 'email', 'sujet', 'date_update', 'status')
    search_fields = ('nom', 'email', 'sujet')
    date_hierarchy = 'date_add'
    list_display_links = ['email', 'nom']
    ordering = ['nom', 'email', 'sujet']
    
    fieldsets = [
        ('Info Contact', {'fields': ['nom', 'email', 'sujet', 'message']}),
        ('Standare', {'fields': ['status']})
    ]



class TemoignageAdmin(Action):
    list_display = ('auteur', 'metier', 'date_update', 'status')
    search_fields = ('auteur', 'metier', 'message')
    date_hierarchy = 'date_add'
    list_display_links = ['auteur', 'metier']
    ordering = ['auteur', 'metier']
    
    fieldsets = [
        ('Info Temoignage', {'fields': ['auteur', 'metier', 'message']}),
        ('Standare', {'fields': ['status']})
    ]



def _register(model, admin_class):
    admin.site.register(model, admin_class)



_register(models.SiteInfo, SiteInfoAdmin)
_register(models.SocialAccount, SocialAccountAdmin)
_register(models.NewsLetter, NewsLetterAdmin)
_register(models.Contact, ContactAdmin)
_register(models.Temoignage, TemoignageAdmin)


