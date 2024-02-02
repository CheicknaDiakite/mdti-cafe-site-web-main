from django.db import models
import datetime, os
from tinymce.models import HTMLField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
def get_file_path(request, filename):
    originale_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, originale_filename)
    return os.path.join('uploads/', filename)

class Categorie(models.Model):
    titre = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=False, blank=True, verbose_name="Image 500x500")
    description = models.TextField(max_length=500, default='')  # Ajout de default=''
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titre
    
    
class Formation(models.Model):
    category = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    titre = models.CharField(max_length=150,null=False,blank=False)
    date_debut = models.DateField()
    date_fin = models.DateField()
    image = models.ImageField(upload_to=get_file_path, null=False, blank=True, verbose_name="Image 500x500")
    description = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titre + " (Nombre de clients  " + str(len(self.client_set.all())) + " )"
    
class Client(models.Model):
    formation = models.ForeignKey(Formation,on_delete=models.CASCADE)
    nom = models.CharField(max_length=150,null=False,blank=False)
    prenom = models.CharField(max_length=150,null=False,blank=False)
    email = models.EmailField(max_length=254)
    numero_telephone = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom