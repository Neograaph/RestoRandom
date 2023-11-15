from django.db import models

class Restaurant(models.Model):
    nom = models.CharField(max_length=255)
    # description = models.TextField()
    # adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nom
