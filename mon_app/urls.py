# mon_app/urls.py
from django.urls import path
from .views import ma_vue
from .views import liste_restaurants, ma_vue_random
from .views import sauvegarder_restaurants

urlpatterns = [
    path('', liste_restaurants, name='liste_restaurants'),
    path('map/', ma_vue, name='ma_vue'),
    path('map/random', ma_vue_random, name='ma_vue_random'),
    path('sauvegarder_restaurants/', sauvegarder_restaurants, name='sauvegarder_restaurants'),
    # path('ajouter_donnees/', ajouter_donnees, name='ajouter_donnees'),
]
