from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categorie)
@admin.register(Actualite)
class AdminActualite(admin.ModelAdmin):
    list_display = ["titre", "category"]
    list_filter = ["category"]
