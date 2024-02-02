from django.contrib import admin

from .models import PresentationModel, AProposModel


# Register your models here.


@admin.register(PresentationModel)
class PresentationModelAdmin(admin.ModelAdmin):
    pass

@admin.register(AProposModel)
class AProposModelModelAdmin(admin.ModelAdmin):
    pass