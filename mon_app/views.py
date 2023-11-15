# mon_app/views.py
from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse
import folium
import requests
from django.shortcuts import render
from .models import Restaurant
from django.views.generic import ListView, UpdateView
from django.urls import reverse
from .models import Restaurant

    
def liste_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'liste_restaurants.html', {'restaurants': restaurants})


def ma_vue(request):
    # Initialiser la carte
    ma_carte = folium.Map(location=[47.88296709996544, 1.9037131], zoom_start=13)

    # Ajouter des tuiles personnalisées avec attribution
    folium.TileLayer(
    tiles='https://{s}.tile.example.com/{z}/{x}/{y}.png',  # Remplacez par votre URL de tuiles personnalisées
    attr='Attribution de vos tuiles personnalisées',
    name='Tuiles personnalisées'
    ).add_to(ma_carte)

    # Ajouter un marqueur
    folium.Marker([47.88296709996544, 1.9037131], popup='CESI Orléans').add_to(ma_carte)

    # Sauvegarder la carte dans un fichier HTML
    ma_carte.save("ma_carte.html")
    
    carte_html = ma_carte.get_root().render()
    return render(request, 'ma_vue_template.html', {'carte_html': carte_html})


# from django.shortcuts import render
# import requests
# import folium
# from django.http import HttpResponse

# def ma_vue(request):
#     # Initialiser la carte
#     ma_carte = folium.Map(location=[47.88296709996544, 1.9037131], zoom_start=13)

#     # Ajouter une couche de tuiles (par exemple, OpenStreetMap)
#     folium.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', attribution='© OpenStreetMap contributors').add_to(ma_carte)

#     # Ajouter un marqueur
#     folium.Marker([47.88296709996544, 1.9037131], popup='CESI Orléans').add_to(ma_carte)

#     json_url = "https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/osm-restaurant-fr@babel/records?limit=100&refine=type%3A%22restaurant%22&refine=commune%3A%22Orl%C3%A9ans%22"

#     response = requests.get(json_url)
#     data = response.json()

#     # Assurez-vous que "records" est présent dans votre fichier JSON
#     if 'records' in data:
#         # Ajouter des marqueurs pour chaque élément dans "records"
#         for record in data['records']:
#             # Assurez-vous que "geometry" est présent dans chaque élément
#             if 'geometry' in record and 'coordinates' in record['geometry']:
#                 lon, lat = record['geometry']['coordinates']
#                 folium.Marker([lat, lon], popup=f"Nom: {record['fields']['name']}<br>Latitude: {lat}<br>Longitude: {lon}").add_to(ma_carte)

#     # Sauvegarder la carte dans un fichier HTML
#     carte_html = ma_carte.get_root().render()
#     return render(request, 'ma_vue_template.html', {'carte_html': carte_html})
