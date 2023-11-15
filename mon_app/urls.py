# mon_app/urls.py
from django.urls import path
from .views import ma_vue
from .views import liste_restaurants

urlpatterns = [
    path('map/', ma_vue, name='ma_vue'),
    path('restaurants/', liste_restaurants, name='liste_restaurants'),
]
