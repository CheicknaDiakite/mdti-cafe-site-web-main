from django.contrib import admin

from .models import DocumentsCoinDuConsultant


# Register your models here.


@admin.register(DocumentsCoinDuConsultant)
class DocumentsCoinDuConsultantAdmin(admin.ModelAdmin):
    pass
