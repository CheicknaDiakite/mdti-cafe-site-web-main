from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request, cateogrie_slug=None):
    # Pour les categories : grouper par categorie
    categories = Categorie.objects.annotate(Count('service'))
    categories = categories.values_list("nom", 'slug', 'service__count')
    # print(categories)

    if cateogrie_slug is not None:
        services = Service.objects.filter(categorie__slug=cateogrie_slug)
    else:
        services = Service.objects.all()

    context = {'services': services, "categories": categories}
    return render(request, 'service/index.html', context)


def servicedetail(request, titre):
    serviceDetail = Service.objects.filter(titre=titre).first()
    context = {'serviceDetail': serviceDetail}
    return render(request, 'service/detail.html', context)
