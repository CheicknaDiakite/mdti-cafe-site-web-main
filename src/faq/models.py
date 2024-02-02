from django.db import models
from tinymce.models import HTMLField


# Create your models here.


class FaqModel(models.Model):
    question = models.CharField(max_length=512, verbose_name="Question*")
    reponse = HTMLField(verbose_name="Reponse à la question*")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (self.question[:20] + '..') if len(self.question) > 20 else self.question

    class Meta:
        verbose_name = "Question-question"
        verbose_name_plural = "Question-questions"