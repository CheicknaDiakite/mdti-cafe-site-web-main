from django.shortcuts import render

from faq.models import FaqModel


# Create your views here.


def faq_index(request):
    all_faq = FaqModel.objects.all()
    return render(request, "faq/index.html", context={"all_faq": all_faq})
