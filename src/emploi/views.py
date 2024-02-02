from os.path import splitext

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from django.contrib import messages
from django.urls import reverse

from outils.mailer import send
from root.settings import TEST_ADMIN_MAIL
from .models import *


# Create your views here.
def emploi_index(request):
    aujourdhui = date.today()
    offres = Emploi.objects.all()
    context = {'offres': offres, 'aujourdhui': aujourdhui}
    return render(request, "emploi/index.html", context)


def emploi_detail(request, titre):
    if (Emploi.objects.filter(titre=titre).exists()):
        offre = Emploi.objects.filter(titre=titre).first()
        context = {'offre': offre}
        return render(request, "emploi/detail.html", context)
    else:
        messages.error(request, "Pas d'offre")
        return redirect('emploi_index')


def postuler(request, id=None):
    all_diplome = Diplome.objects.all()
    emploi = Emploi.objects.filter(id=id).first()
    context = {"id": id, "all_diplome": all_diplome, "emploi": emploi}
    if request.method == "POST":
        emploi = Emploi.objects.filter(id=id).first()

        if emploi is not None:
            new_candidat = Candidat()

            new_candidat.nom = request.POST.get("nom")
            new_candidat.prenom = request.POST.get("prenom")
            new_candidat.email = request.POST.get("email")
            new_candidat.numero = request.POST.get("numero")

            dernier_diplome = Diplome.objects.filter(id=request.POST.get("dernier_diplome")).first()
            # TODO verifier si le dernier_diplome existe
            new_candidat.dernier_diplome = dernier_diplome
            new_candidat.date_naissance = request.POST.get("date_naissance")
            new_candidat.emploi = emploi

            new_candidat.save()
            # print(f"numero {request.POST.get('numero')}")

            # TODO DEBUG remove apres
            print(len(request.FILES.getlist('files')))
            print(request.FILES.getlist('files'))
            # print(request.FILES)

            for file in request.FILES.getlist('files'):
                tmp_doc = Document()
                tmp_doc.nom = splitext(file.name)[0]
                tmp_doc.candidat = new_candidat
                tmp_doc.document = file
                tmp_doc.save()

                # TODO DEBUG remove apres
                print(splitext(file.name)[0])

            # TODO à modifier plus tard
            # Informer l'administrateur
            send(sujet="Nouvelle Candidature",
                 message=f"Une personne vient de postuler à l'offre : {emploi.titre}",
                 email_liste=TEST_ADMIN_MAIL)

            # Informer le visiteur
            send(sujet="Inscription prise en compte",
                 message=f"Bonjour {new_candidat.nom} {new_candidat.prenom}, Votre candidature a été bien reçue",
                 email_liste=[new_candidat.email])

            messages.success(request, "Merci, votre candidature a été prise en compte")
            return redirect('/')

        else:
            pass

    else:
        return render(request, "emploi/postuler.html", context)


def download(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    response = HttpResponse(document.document, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.document.name}"'
    return response


def send_mail_to_candidat(request):
    if 'envoyer' in request.POST:
        email_list = request.POST.get("email_list").split(",")
        candidature_id_list = request.POST.get("candidature_id_list").split(",")

        message = request.POST.get("message")
        sujet = request.POST.get("sujet")
        next = request.POST.get("next")

        # TODO verifier la valeur retounee
        send(sujet=sujet,
             message=message,
             email_liste=email_list)

        # set contacter
        for id in candidature_id_list:
            candidat_tmp = Candidat.objects.filter(id=id).first()
            if candidat_tmp is not None:
                candidat_tmp.contacter = True
                candidat_tmp.save()

        # TODO debug a effacer
        print(email_list)
        messages.success(request, "Email envoyé")
        return HttpResponseRedirect(next)


def profile_candidat(request):
    if request.user.is_authenticated:
        return render(request, "emploi/profile_candidat.html")

    return redirect(reverse("my_login"))

