from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name="contact_index"),
    path('contact_form',views.contact_form,name="contact_form"),
]