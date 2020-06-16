
from django.urls import path
from . import views

urlpatterns = [
    path('', views.service, name='service'),
    path('apartment/', views.apartment, name='apartment'),
    path('project', views.project, name='project'),
]
