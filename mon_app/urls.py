# mon_app/urls.py
from django.urls import path
from .views import MonModeleListCreateView
from .views import ma_vue

urlpatterns = [
    path('', MonModeleListCreateView.as_view(), name='monmodele-list-create'),
    path('test/', ma_vue, name='ma_vue'),
]
