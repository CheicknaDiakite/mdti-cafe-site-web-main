from django.shortcuts import render

# Create your views here.


def profile_recruteur(request):
    return render(request,"coin_du_recurteur/profil_recruteur.html")

