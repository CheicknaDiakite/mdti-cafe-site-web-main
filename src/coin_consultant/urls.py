from django.urls import path

from .views import index, download

urlpatterns = [
    path("", index, name="coin_consultant"),
    path('download/<int:document_id>/', download, name='download'),  # Lien pour telecharger les document
]
