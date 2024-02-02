from django.contrib import admin
from django.forms import forms

from .models import *


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'sujet', 'message', "repondu")
    fields = ('name', 'email', 'sujet', 'message', "repondu", "reponse")

    def has_add_permission(self, request, obj=None):
        return False
