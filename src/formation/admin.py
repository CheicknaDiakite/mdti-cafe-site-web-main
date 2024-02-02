from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Categorie)
@admin.register(Formation)
class AdminFormation(admin.ModelAdmin):
    list_display = ["titre"]
    list_filter = ["category"]

@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ["nom", "prenom", "numero_telephone"]
    list_filter = ["formation"]
