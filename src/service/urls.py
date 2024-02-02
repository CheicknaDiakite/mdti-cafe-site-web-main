from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='service_index'),
    path('<str:cateogrie_slug>', views.index, name='service_index_by_categorie'),
    path('<str:titre>/detail', views.servicedetail, name="servicedetail"),
]
