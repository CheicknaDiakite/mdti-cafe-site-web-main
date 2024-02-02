from django.contrib import admin

from .models import ReseauSocial, Membre, Poste


# Register your models here.


@admin.register(ReseauSocial)
class AdminReseauSocial(admin.ModelAdmin):
    pass

@admin.register(Membre)
class AdminMembre(admin.ModelAdmin):
    list_display = ["nom", "prenom", "numero"]
    list_filter = ["poste"]

@admin.register(Poste)
class AdminPoste(admin.ModelAdmin):
    pass