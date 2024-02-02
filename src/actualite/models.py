from django.db import models


# Create your models here.
import datetime
import os

from compte.models import Utilisateur


def get_file_path(request,filename):
    originale_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, originale_filename)
    return os.path.join('uploads/',filename)

class Categorie(models.Model):
    titre = models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titre
    
    
class Actualite(models.Model):
    category = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    user = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    titre = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=False, blank=True, verbose_name="Image 1200x700")
    description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titre