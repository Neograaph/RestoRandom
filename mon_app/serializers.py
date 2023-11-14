# mon_app/serializers.py
from rest_framework import serializers
from .models import MonModele

class MonModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonModele
        fields = '__all__'
