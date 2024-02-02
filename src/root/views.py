
from django.shortcuts import render

from actualite.models import Actualite
from equipe.models import Membre
from faq.models import FaqModel
from outils.mailer import send
from presentation.models import AProposModel
from service.models import *
from slider.models import *


def base_index(request):
    apropos_video = AProposModel.objects.all()
    all_faq = FaqModel.objects.all()
    services = Service.objects.all()
    actualite = Actualite.objects.all()
    sliders = Slider.objects.all()
    #recup équipe
    membres = Membre.objects.all()
    context = {'services': services, "apropos_video": apropos_video, "all_faq": all_faq,"actualite":actualite,"membres":membres,"sliders":sliders}
    return render(request, "index.html", context)

# pour les video et l'image
