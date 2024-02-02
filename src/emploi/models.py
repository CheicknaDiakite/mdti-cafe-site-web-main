from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField
import datetime, os


# Create your models here.
def get_file_path(request, filename):
    originale_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H/%M/%S')
    filename = "%s%s" % (nowTime, originale_filename)
    return os.path.join('uploads/', filename)


class Diplome(models.Model):
    nom = models.CharField(max_length=30)
    priorite = models.PositiveIntegerField()
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.nom


class Emploi(models.Model):
    titre = models.CharField(max_length=300, verbose_name="Titre")
    date_limite = models.DateField(verbose_name="Date limite")
    date = models.DateField(auto_now=True, editable=False)
    image = models.ImageField(upload_to=get_file_path, verbose_name="Image 1200x700")
    description = HTMLField()
    niveau_minimum = models.ForeignKey(Diplome, on_delete=models.SET_NULL, null=True, verbose_name="Diplome requis")

    def __str__(self):
        return self.titre


class Candidat(models.Model):
    nom = models.CharField(max_length=300)
    prenom = models.CharField(max_length=300)
    sexe = models.CharField(max_length=30,verbose_name="Genre")
    quartier = models.CharField(max_length=300,verbose_name="Quartier / ville")
    date_naissance = models.DateField()
    date_candidature = models.DateField(auto_now=True, verbose_name="Date de candidature")
    email = models.EmailField()
    numero = models.CharField(max_length=200)
    dernier_diplome = models.ForeignKey(Diplome, on_delete=models.SET_NULL, null=True)
    emploi = models.ForeignKey(Emploi, on_delete=models.CASCADE, null=True)
    contacter = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

    @property
    def document(self):
        return self.document_set.all()
        # return ",".join([ mark_safe(f"<a href='{p.document.url}' > p.document.nom</a>") for p in self.document_set.all()])

    @property
    def nom_emploi(self):
        return self.emploi.titre


class Document(models.Model):
    nom = models.CharField(max_length=300)
    document = models.FileField(upload_to=get_file_path)
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
