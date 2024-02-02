from django.urls import path

from faq.views import faq_index

urlpatterns = [
    path("",faq_index, name="faq")
]