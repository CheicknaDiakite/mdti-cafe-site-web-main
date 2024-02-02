from django.shortcuts import render, redirect
from django.contrib import messages
from outils.mailer import send
from root.settings import TEST_ADMIN_MAIL
from django.core.exceptions import ObjectDoesNotExist
from .models import *


# Create your views here.
def index(request):
    categorie = Categorie.objects.all()
    context = {'categorie': categorie}
    return render(request, 'formation/index.html', context)


def categorie_formation(request, titre):
    if (Categorie.objects.filter(titre=titre)):
        formations = Formation.objects.filter(category__titre=titre)
        categorie = Categorie.objects.filter(titre=titre).first()
        context = {'formations': formations, 'categorie': categorie}
        return render(request, 'formation/detail.html', context)
    else:
        return redirect('formation_index')


def formation_detail(request, titre, formation_titre):
    formation_detail = Formation.objects.filter(titre=formation_titre).first()
    categorie = Categorie.objects.filter(titre=titre).first()
    context = {'formation_detail': formation_detail, 'categorie': categorie}
    return render(request, 'formation/formation_detail.html', context)


def inscription(request, titre, formation_titre):
    if request.method == 'POST':
        try:
            formation = Formation.objects.get(titre=formation_titre)
            categorie = Categorie.objects.get(titre=titre)

            if Client.objects.filter(email=request.POST.get('email'), formation=formation.id).exists():
                messages.warning(request, "Vous êtes déjà inscrit à cette formation")
                return redirect('/')
            else:
                client = Client()
                client.formation = formation
                client.nom = request.POST.get('nom')
                client.prenom = request.POST.get('prenom')
                client.email = request.POST.get('email')
                client.numero_telephone = request.POST.get('telephone')
                client.message = request.POST.get('message')
                client.save()

                # TODO à modifier plus tard
                # Informer l'administrateur
                send(sujet="Nouvelle inscription",
                     message=f"Une personne vient de s'inscrire à la formation : {formation.titre}",
                     email_liste=TEST_ADMIN_MAIL)

                # Informer le visiteur
                send(sujet="Inscription prise en compte",
                     message=f"Bonjour {client.nom} {client.prenom}, Votre inscription a été bien reçue",
                     email_liste=[client.email])
                messages.success(request, "Merci, votre inscription a été prise en compte")
                return redirect('/')
        except ObjectDoesNotExist:
            messages.error(request, "La formation ou la catégorie spécifiée n'existe pas")
            return redirect('/')
        except Exception as e:
            messages.error(request, "Une erreur s'est produite lors du traitement de votre inscription.")
            return redirect('/')
    else:
        try:
            formation = Formation.objects.get(titre=formation_titre)
            categorie = Categorie.objects.get(titre=titre)
            context = {'formation': formation, 'categorie': categorie}
            return render(request, 'formation/inscription.html', context)
        except ObjectDoesNotExist:
            messages.error(request, "La formation ou la catégorie spécifiée n'existe pas")
            return redirect('/')


