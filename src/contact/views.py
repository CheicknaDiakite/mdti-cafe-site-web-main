from django.shortcuts import render,redirect
from django.contrib import messages
from outils.mailer import send
from root.settings import TEST_ADMIN_MAIL
from .models import *

# Create your views here.
def index(request):
    return render(request, "contact/index.html")

def contact_form(request):
    if request.method == 'POST':
        nouveau_contact = Contact()  # Instanciez un nouvel objet Contact
        nouveau_contact.name = request.POST.get('name')
        nouveau_contact.email = request.POST.get('email')
        nouveau_contact.sujet = request.POST.get('sujet')
        nouveau_contact.message = request.POST.get('message')
        nouveau_contact.save()  # Enregistrez le nouveau contact dans la base de données


        #Envoyer un mail a l'admin
        #TODO changer le mail
        # Informer l'administrateur
        send(sujet=nouveau_contact.sujet, message=nouveau_contact.message, email_liste=TEST_ADMIN_MAIL)

        # Informer le visiteur
        send(sujet="Réception de contact", message=f"Bonjour {nouveau_contact.name}, Votre message a été bien reçu", email_liste=[nouveau_contact.email])

        messages.warning(request, "Merci votre demande a ete prise en compte")
        return redirect('/')
    else:
        return render(request, 'index.html')  # Affichez le formulaire pour les requêtes GET