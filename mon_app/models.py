from django.db import models

class MonModele(models.Model):
    champ1 = models.CharField(max_length=100)
    champ2 = models.IntegerField()
    # Ajoutez d'autres champs selon vos besoins
