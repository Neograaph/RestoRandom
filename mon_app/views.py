# mon_app/views.py
from rest_framework import generics
from .models import MonModele
from .serializers import MonModeleSerializer
from django.shortcuts import render
from django.http import HttpResponse

class MonModeleListCreateView(generics.ListCreateAPIView):
    queryset = MonModele.objects.all()
    serializer_class = MonModeleSerializer

def ma_vue(request):
    return HttpResponse("Bonjour, ceci est une nouvelle vue !")
