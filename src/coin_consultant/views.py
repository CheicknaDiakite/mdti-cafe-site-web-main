from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import DocumentsCoinDuConsultant


# Create your views here.


# TODO documentation ici
def index(request):
    all_document = DocumentsCoinDuConsultant.objects.all()
    return render(request, "coin_consultant/index.html",
                  context={"titire": "Coin du consultant", "all_document": all_document})


def download(request, document_id):
    document = get_object_or_404(DocumentsCoinDuConsultant, pk=document_id)
    response = HttpResponse(document.document, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.document.name}"'
    return response
