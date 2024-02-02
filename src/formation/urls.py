from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="formation_index"),
    path('<str:titre>', views.categorie_formation, name="categorie_formation"),
    path('<str:titre>/<str:formation_titre>', views.formation_detail, name="formation_detail"),
    path('<str:titre>/<str:formation_titre>/inscription', views.inscription, name="inscription")
]