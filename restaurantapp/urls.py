from unicodedata import name
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.api_client, name='api_client'),
    path('menu', views.api_menu, name='api_menu'),    
    path('commande', views.api_commande, name='api_commande'),    

]