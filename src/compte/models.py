from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Utilisateur(AbstractUser):
    TYPE_COMPTE = [("admin","Admin"),("recruteur","Recruteur"),("candidat","Candidat")]

    type_compte = models.CharField(max_length=300,choices=TYPE_COMPTE)
    numero = models.CharField(max_length=200,blank=True, null=True)
    sexe = models.CharField(max_length=30, verbose_name="Genre", blank=True, null=True)
    quartier = models.CharField(max_length=300, verbose_name="Quartier / ville",blank=True, null=True)
    date_naissance = models.DateField(blank=True,null=True)
