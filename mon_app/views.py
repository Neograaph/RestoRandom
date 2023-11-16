# mon_app/views.py
from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse
import folium
import requests
from django.shortcuts import render
from .models import Restaurant, CurrentLocation
from django.views.generic import ListView, UpdateView
from django.urls import reverse


import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


def sauvegarder_restaurants(request):
    # Remplacez l'URL de l'API par celle que vous utilisez
    api_url = 'https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/osm-restaurant-fr@babel/records?limit=100&refine=type%3A%22restaurant%22&refine=commune%3A%22Orl%C3%A9ans%22'
    
    # Effectuez la requête à l'API
    response = requests.get(api_url)
    
    # Vérifiez si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        data = response.json()
        restaurants = data.get('results', [])

        print("Structure des données de l'API :")
        print(data)

        for restaurant_data in restaurants:
            Restaurant.objects.create(
                nom=restaurant_data['name'],
                ville=restaurant_data['commune'],
                code_postal=restaurant_data['code_commune'],
                latitude=restaurant_data['geo_point_2d']['lat'],
                longitude=restaurant_data['geo_point_2d']['lon']
            )
            
        # Répondez avec un message de réussite ou redirigez vers une autre page
        return render(request, 'succes.html', {'message': 'Données sauvegardées avec succès'})
    else:
        # Gérez les erreurs de requête API
        return render(request, 'erreur.html', {'message': 'Erreur lors de la récupération des données'})


def liste_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'liste_restaurants.html', {'restaurants': restaurants})


# from .models import CurrentLocation

# def update_current_location(latitude, longitude):
#     current_location, created = CurrentLocation.objects.get_or_create(id=1)
#     current_location.latitude = latitude
#     current_location.longitude = longitude
#     current_location.save()

# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse

# @csrf_exempt
# def ajouter_donnees(request):
#     if request.method == 'POST':
#         # Récupérez les données du corps de la requête JSON
#         data = request.POST.get('votre_champ')
        
#         # Ajoutez les données à la base de données
#         CurrentLocation.objects.create(votre_champ=data)

#         return JsonResponse({'status': 'success'})
#     else:
#         return JsonResponse({'status': 'error'})

def ma_vue(request):
    # Initialiser la carte
    last_location = CurrentLocation.objects.last()
    print(last_location.latitude)
    print(last_location)
    if last_location:
        ma_carte = folium.Map(location=[last_location.latitude, last_location.longitude], zoom_start=13)
        # Initialiser la carte avec la dernière position enregistrée
    else:
        # Si aucune position n'est enregistrée, utilisez une position par défaut
        ma_carte = folium.Map(location=[47.9027336, 1.9086066], zoom_start=13)
    # folium.Marker(CurrentLocation.latitude, CurrentLocation.longitude, popup='Votre position actuelle').add_to(ma_carte)
    # print(current_location['latitude'], current_location['longitude'])
    # Ajouter des tuiles personnalisées avec attribution
    folium.TileLayer(
    tiles='https://{s}.tile.example.com/{z}/{x}/{y}.png',  # Remplacez par votre URL de tuiles personnalisées
    attr='Attribution de vos tuiles personnalisées',
    name='Tuiles personnalisées'
    ).add_to(ma_carte)

    # Ajouter un marqueur
    # folium.Marker([47.8449784, 1.9405153], popup='CESI Orléans').icon=folium.Icon("red").add_to(ma_carte)
    folium.Marker(
    location=[47.8449784, 1.9405153],
    tooltip="Vous êtes ici",
    popup="Géolocalisation : 1 Allée du Titane, 45100 Orléans, France",
    icon=folium.Icon(icon="cloud"),
).add_to(ma_carte)

    restaurants = Restaurant.objects.all()
    for restaurant in restaurants:
        folium.Marker([restaurant.latitude, restaurant.longitude], popup=restaurant.nom).add_to(ma_carte)

    # Sauvegarder la carte dans un fichier HTML
    # ma_carte.save("ma_carte.html")
    
    
    carte_html = ma_carte.get_root().render()
    return render(request, 'map.html', {'carte_html': carte_html})

from django.shortcuts import render
import folium
from .models import Restaurant
from django.http import JsonResponse
import random
from .forms import RandomRestaurantForm

def ma_vue_random(request):
    if request.method == 'POST':
        form = RandomRestaurantForm(request.POST)
        if form.is_valid():
            # Choisissez un restaurant au hasard
            restaurants = Restaurant.objects.all()
            restaurant_choisi = random.choice(restaurants)

            # Initialiser la carte avec la position du restaurant choisi
            ma_carte = folium.Map(location=[restaurant_choisi.latitude, restaurant_choisi.longitude], zoom_start=18)

            # Ajoutez des tuiles personnalisées avec attribution
            folium.TileLayer(
                tiles='https://{s}.tile.example.com/{z}/{x}/{y}.png',  # Remplacez par votre URL de tuiles personnalisées
                attr='Attribution de vos tuiles personnalisées',
                name='Tuiles personnalisées'
            ).add_to(ma_carte)

            # Ajoutez un marqueur pour le restaurant choisi
            folium.Marker([restaurant_choisi.latitude, restaurant_choisi.longitude], popup=restaurant_choisi.nom).add_to(ma_carte)

            # Ajoutez des marqueurs pour les autres restaurants
            for restaurant in restaurants.exclude(id=restaurant_choisi.id):
                folium.Marker([restaurant.latitude, restaurant.longitude], popup=restaurant.nom).add_to(ma_carte)

            # Sauvegardez la carte dans un fichier HTML (facultatif)
            carte_html = ma_carte.get_root().render()
            return render(request, 'map.html', {'carte_html': carte_html, 'form': form})
    else:
        form = RandomRestaurantForm()

    return render(request, 'map.html', {'form': form})