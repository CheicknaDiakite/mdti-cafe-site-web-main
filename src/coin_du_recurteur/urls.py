from django.urls import path

from coin_du_recurteur.views import profile_recruteur

urlpatterns = [

    path('profile',profile_recruteur, name="profile_recruteur")
]