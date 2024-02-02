from django.contrib import admin

from faq.models import FaqModel


# Register your models here.

@admin.register(FaqModel)
class AProposModelModelAdmin(admin.ModelAdmin):
    pass