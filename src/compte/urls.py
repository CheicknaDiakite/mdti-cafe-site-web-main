from django.urls import path, include

from .views import my_login, my_inscription, mot_de_passe_oublier, my_logout

urlpatterns = [
    path('connexion', my_login, name="my_login"),
    path('inscription', my_inscription, name="my_inscription"),
    path('deconnexion', my_logout, name="my_logout"),
    path('mot-de-passe-oublier', mot_de_passe_oublier, name="mot_de_passe_oublier")
]
