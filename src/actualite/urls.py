from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="actualite_index"),
    path('<str:titre>', views.detailActualite, name="detailActualite"),
    path('d/<str:annee>', views.index, name="actualite_index"),
]
