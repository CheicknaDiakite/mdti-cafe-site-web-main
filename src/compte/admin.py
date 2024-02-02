from django.contrib import admin

from compte.models import Utilisateur


# Register your models here.


@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    ...
