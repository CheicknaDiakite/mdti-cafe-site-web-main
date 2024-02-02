from django.db import models
import datetime
import os

# Create your models here.
def get_file_path(request,filename):
    originale_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, originale_filename)
    return os.path.join('uploads/',filename)

class Slider(models.Model):
    titre = models.CharField(max_length=150)
    reference = models.TextField(max_length=500,default= '')
    image = models.ImageField(upload_to=get_file_path, verbose_name="Image 1920x1080")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titre
