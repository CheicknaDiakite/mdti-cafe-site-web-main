from django.db import models
import datetime, os

from django.utils.text import slugify


# Create your models here.

def get_file_path(request, filename):
    originale_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, originale_filename)
    return os.path.join('uploads/', filename)


class Categorie(models.Model):
    nom = models.CharField(max_length=300)
    slug = models.SlugField(editable=False)
    image = models.ImageField(upload_to=get_file_path, verbose_name="Image 500x500")

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        #recherche d'un slug unique
        slug = slugify(self.nom)
        unique_slug = slug
        num = 1
        while Categorie.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1

        self.slug = slug
        super().save(self, *args, **kwargs)




class Service(models.Model):
    titre = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=False, blank=True, verbose_name="Image 500x500")
    description = models.TextField(max_length=500, null=False, blank=False)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
