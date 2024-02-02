from django.shortcuts import render

from .models import PresentationModel

# Create your views here.


"""

"""


def index(request):
    """
    :on par du principe que le nombre de presentation est 1 sinon on recup le premier
    :param request:
    :return:
    """
    # recuperation du premier (ou la seule ) puis on vérifie s'il existe sinon un message l'indiquant
    presentation = PresentationModel.objects.first()
    if presentation is None:
        presentation = "<p>Pas de présentation pour le moment</p>"
    else:
        presentation = presentation.contenue

    return render(request, "presentation/index.html",
                  context={"titire": "Coin du consultant", "presentation": presentation})
