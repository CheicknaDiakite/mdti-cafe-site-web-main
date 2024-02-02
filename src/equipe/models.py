from django.db import models

# Create your models here.

RESEUX_LISTE = [
    ("twitter","Twitter"),
    ("facebook","Facebook"),
    ("instagram","Instagram"),
    ("linkedIn","LinkedIn")
]

class Poste(models.Model):
    nom = models.CharField(max_length=300,unique=True,verbose_name="Nom du poste")

    def __str__(self):
        return self.nom


class Membre(models.Model):
    nom = models.CharField(max_length=300)
    prenom = models.CharField(max_length=300, verbose_name="Prénom")
    poste = models.ForeignKey(Poste,on_delete=models.SET_NULL,null=True, verbose_name="Le poste")
    numero = models.CharField(max_length=20, verbose_name='Numéro de téléphone') # utilise une librairie externe à django
    image = models.ImageField(upload_to="equipe/%Y/%m/%d", verbose_name="Image 500x500")

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class ReseauSocial(models.Model):
    nom_reseau = models.CharField(max_length=40,choices=RESEUX_LISTE)
    url = models.URLField(max_length=300, unique=True)
    proprietaire = models.ForeignKey(Membre,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom_reseau} - {self.proprietaire.nom}"