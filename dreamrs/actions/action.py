# coding: utf-8

from django.contrib import admin

"""
       Utilisation dans une application (models.py)
       ____________________________________________

from actions.action import Action

class MyModelAdmin(Action):
    ...
    
"""

class Action(admin.ModelAdmin):

    actions = ["activate", "deactivate"]

    def deactivate(self, request, queryset):

        queryset.update(status=False)

        # Message a afficher a l'utilisateur apres realisation de l'action
        self.message_user(request, "Désactivation(s) effectué(s)")

    # Renomage de l'action de maniere plus estethique
    deactivate.short_description = "Désactiver les elements selectionnés"

    def activate(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "Activation(s) effectué(s)")
    activate.short_description = "Activer les elements selectionnés"
