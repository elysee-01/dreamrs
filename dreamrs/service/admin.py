from django.contrib import admin

# Register your models here.
from . import models

from django.utils.safestring import mark_safe

from actions.action import Action


class ServiceAdmin(Action):
    list_display = ('nom', 'date_add', 'date_update',
                    'status', 'images_view')
    list_filter = ('status', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Service', {'fields': ['nom', 'image', 'description']}),
                 ('Standare', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))



class ProjectTypeAdmin(Action):
    list_display = ('name', 'date_update', 'status')
    list_filter = ('name',)
    search_fields = ('name', )
    date_hierarchy = 'date_add'
    list_display_links = ['name']
    ordering = ['name']
    list_per_page = 10
    
    fieldsets = [
        ('Info ProjectType', {'fields': ['name']}),
        ('Standare', {'fields': ['status']})
    ]



class ProjectAdmin(Action):
    list_display = ('titre', 'type_projet', 'nouveau_projet', 'date_update',
                    'status')
    list_filter = ('type_projet', 'status', 'nouveau_projet')
    search_fields = ('type_projet', )
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    
    fieldsets = [
        ('Info Project', {'fields': ['titre', 'type_projet', 'nouveau_projet']}),
        ('Standare', {'fields': ['status']})
    ]



class ApartmentAdmin(Action):
    list_display = ('type_apart', 'nombre_salle_bain', 'nombre_chambre', 
                    'date_update', 'nombre_fenetre', 'status')
    list_filter = ('type_apart', )
    search_fields = ('type_apart', 'nombre_salle_bain', 'nombre_chambre', 'nombre_fenetre')
    date_hierarchy = 'date_add'
    list_display_links = ['type_apart']
    ordering = ['type_apart']
    list_per_page = 10
    
    fieldsets = [
        ('Info Project', {'fields': ['type_apart', 'nombre_salle_bain', 'nombre_chambre', 'nombre_fenetre', 'description']}),
        ('Standare', {'fields': ['status']})
    ]



def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Service, ServiceAdmin)
_register(models.ProjectType, ProjectTypeAdmin)
_register(models.Project, ProjectAdmin)
_register(models.Apartment, ApartmentAdmin)