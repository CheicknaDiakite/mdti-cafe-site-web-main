from django.urls import path

from admin_personnaliser.views import profile_admin

urlpatterns = [

    path('profile',profile_admin, name="profile_admin")
]