from django.urls import path, include
from .views import *

urlpatterns = [
    path('', emploi_index, name="emploi_index"),
    path('detail/<str:titre>', emploi_detail, name="emploi_detail"),
    path('postuler/<str:id>', postuler, name="postuler"),
    path('download/<int:document_id>/', download, name='download_cv'),  # Lien pour telecharger les document
    path('send-mail/', send_mail_to_candidat, name='send_mail_to_candidat'),  # Lien pour telecharger les document

    path('profile',profile_candidat, name="profile_candidat")
]