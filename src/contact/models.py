from django.db import models

from outils.mailer import send


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False,verbose_name="Nom")
    email = models.EmailField(max_length=150, null=False, blank=False)
    sujet = models.CharField(max_length=150, null=False, blank=False)
    message = models.TextField(max_length=500, null=False, blank=False)
    repondu = models.BooleanField(default=False, verbose_name="Répondu")
    reponse = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.reponse and not self.repondu:
            send(sujet=f"{self.sujet}",
                 message=f"{self.reponse}", email_liste=[self.email])
            self.repondu = True
        super().save(*args, **kwargs)
