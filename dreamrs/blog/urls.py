
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<str:filtre>/<int:filtre_id>/', views.blog, name='blog'),
    path('search/', views.search, name='search'),
    path('<int:article_id>/single/', views.single, name='single'),
]
