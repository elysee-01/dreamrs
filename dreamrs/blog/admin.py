from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe

from actions.action import Action


class ArticleInline(admin.TabularInline):
    model = models.Article
    extra = 1


class CathegorieArticleAdmin(Action):
    list_display = ('nom', 'date_add', 'date_update',
                    'status')
    list_filter = ('status', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Cathegorie', {'fields': ['nom']}),
                 ('Standare', {'fields': ['status']})
                 ]
    inlines = [ArticleInline]


class TagAdmin(Action):
    list_display = ('nom', 'date_add', 'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Tag', {'fields': ['nom']}),
                 ('Standare', {'fields': ['status']})
                 ]


class ArticleAdmin(Action):
    list_display = ('titre', 'cathegorie', 'auteur', 'date_add', 'date_update',
                    'status', 'images_view')
    list_filter = ('status', )
    search_fields = ('titre', )
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    fieldsets = [('Info Article', {'fields': ['auteur', 'titre', 'description', 'contenu', 'image', 'cathegorie', 'tag']}),
                 ('Standare', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class CommentaireAdmin(Action):
    list_display = ('article', 'auteur', 'date_add',
                    'date_update', 'status', 'images_view')
    list_filter = ('status', )
    search_fields = ('article', )
    date_hierarchy = 'date_add'
    list_display_links = ['article']
    ordering = ['article']
    list_per_page = 10
    fieldsets = [('Info Commentaire', {'fields': ['article', 'auteur', 'commentaire']}),
                 ('Standare', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.auteur.photo.url}" style="height:50px; width:100px">')


class InstagramFeedAdmin(Action):
    list_display = ('date_add', 'date_update', 'status', 'images_view')
    list_filter = ('status', )
    date_hierarchy = 'date_add'
    list_display_links = ['images_view']
    ordering = ['date_update']
    list_per_page = 10
    fieldsets = [('Info Commentaire', {'fields': ['image']}),
                 ('Standare', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:100px">')



def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Tag, TagAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.InstagramFeed, InstagramFeedAdmin)
_register(models.CathegorieArticle, CathegorieArticleAdmin)
