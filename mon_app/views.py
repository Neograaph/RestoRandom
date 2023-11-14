# mon_app/views.py
from rest_framework import generics
from .models import MonModele
from .serializers import MonModeleSerializer

class MonModeleListCreateView(generics.ListCreateAPIView):
    queryset = MonModele.objects.all()
    serializer_class = MonModeleSerializer
