# mon_app/urls.py
from django.urls import path
from .views import ma_vue
from .views import liste_restaurants
from .views import sauvegarder_restaurants, ajouter_donnees

urlpatterns = [
    path('map/', ma_vue, name='ma_vue'),
    path('restaurants/', liste_restaurants, name='liste_restaurants'),
    path('sauvegarder_restaurants/', sauvegarder_restaurants, name='sauvegarder_restaurants'),
    path('ajouter_donnees/', ajouter_donnees, name='ajouter_donnees'),
]
