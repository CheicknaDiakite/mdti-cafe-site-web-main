from django.db import models

from compte.models import Utilisateur


# Create your models here.

class DocumentsCoinDuConsultant(models.Model):
    author = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True)
    nom_document = models.CharField(max_length=300, verbose_name="Nom du document")
    document = models.FileField(upload_to="document/%Y/%M/%d", verbose_name="Le document")
    description = models.TextField(max_length=512)
    created_date = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Document"

    def __str__(self):
        return self.nom_document
