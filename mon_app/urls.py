# mon_app/urls.py
from django.urls import path
from .views import MonModeleListCreateView

urlpatterns = [
    path('monmodele/', MonModeleListCreateView.as_view(), name='monmodele-list-create'),
]
