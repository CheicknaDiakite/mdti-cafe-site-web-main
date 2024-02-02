from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def index(request,annee=None):
    #Pour les archives : grouper par mois
    archives = Actualite.objects.annotate(mois=TruncMonth('created_at')).values('mois').annotate(nombre=Count('id')).values('mois', 'nombre')
    # print(archives)
    # d = datetime.date.month
    # print(d)

    #
    if annee is not None:
        year = annee[0:4]
        # print(year)
        month = annee[5:7]
        # print(month)
        actualite = Actualite.objects.filter(created_at__year=year, created_at__month=month)

    else:
        actualite = Actualite.objects.all()

    context = {'actualite': actualite,"archives":archives}
    return render(request, 'actualite/index.html',context)

def detailActualite(request,titre):
    detailActualite = Actualite.objects.filter(titre=titre).first()
    context = {'detailActualite': detailActualite}
    return render(request, 'actualite/detail.html',context)


def get_actualite_by_month_and_year(request,annee):
    #Pour les archives : grouper par mois
    archives = Actualite.objects.annotate(mois=TruncMonth('created_at')).values('mois').annotate(nombre=Count('id')).values('mois', 'nombre')
    # print(archives)

    year = annee[0:4]
    # print(year)

    month = annee[5:7]
    # print(month)


    # return JsonResponse({"year":year,"month":month})
    actualite = Actualite.objects.filter(created_at__year=year,created_at__month=month)
    context = {'actualite': actualite,"archives":archives}
    return render(request, 'actualite/index.html',context)

