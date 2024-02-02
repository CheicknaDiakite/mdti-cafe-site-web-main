from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.safestring import mark_safe

from emploi.models import Diplome, Emploi, Candidat, Document
from outils.mailer import send


# Register your models here.

@admin.register(Diplome)
class DiplomeAdmin(admin.ModelAdmin):
    list_display = ["nom"]
    list_filter = ["priorite"]


@admin.register(Emploi)
class EmploiAdmin(admin.ModelAdmin):
    list_display = ["titre", "date"]
    list_filter = ["niveau_minimum"]


@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin):
    list_display = ["nom", "prenom", "numero", "email", "contacter", "dernier_diplome", "priorite_par_diplome"]

    readonly_fields = ["nom", "prenom", "document"]
    actions = ["envoyer_un_email"]
    list_filter = ["emploi","contacter","dernier_diplome"]

    def envoyer_un_email(self, request, queryset):

        email_list = []
        candidature_id_list = []
        for candidat in queryset:
            email_list.append(candidat.email)
            candidature_id_list.append(str(candidat.id))

        context = {
            "queryset": queryset,
            "next": request.get_full_path(),
            "email_list": ",".join(email_list),
            "candidature_id_list": ",".join(candidature_id_list),
        }

        return render(request, "admin/message_au_candidat.html", context=context)

    def document(self, obj):
        display_text = " ; ".join([
            f"<a href='/emploi/download/{doc.id}' >{doc.nom}</a>"
            for doc in obj.document
        ])
        if display_text:
            return mark_safe(display_text)
        return "-"

    def priorite_par_diplome(self, obj):
        return obj.dernier_diplome.priorite

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False



# pas la peine
# @admin.register(Document)
# class DocumentAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request, obj=None):
#         return False
