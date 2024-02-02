from django.db import models
from django.forms import forms
from tinymce.models import HTMLField


# Create your models here.


# La description
class PresentationModel(models.Model):
    contenue = HTMLField(verbose_name="Présentation",
                         help_text="L'ancien s'il existe sera ecrasé \n il ne peut y avoir qu'une seule présentation")
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Presentation N° {self.pk}"

    class Meta:
        verbose_name = "Présentation de CAFE SARL"
        verbose_name_plural = "Présentation de CAFE SARL"

    # pour éviter d'avoir plusieur présentation on supprimer l'ancien
    def clean(self):
        if len(PresentationModel.objects.all()) >= 1:
            PresentationModel.objects.all().delete()


class AProposModel(models.Model):
    description = HTMLField()
    image = models.ImageField(upload_to="image/%Y/%M/%d", verbose_name="Image de couverture 1200x700")
    lienVideoYoutube = models.URLField(max_length=1024, verbose_name="Lien youtube de la video",blank=True, null=True)
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "A propos de CAFE SARL"
        verbose_name_plural = "A propos de CAFE SARL"

    def clean(self):
        if len(AProposModel.objects.all()) > 2:
            AProposModel.objects.first().delete()
