from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse

from compte.models import Utilisateur


# Create your views here.

def my_login(request):

    # TODO vers la page correspondante
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("/admin")
        if True:
            return render(request, "emploi/profile_candidat.html")

    if request.method == "POST":
        post = request.POST
        username = post.get("username")
        password = post.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            messages.success(request, "Mercie, Vous êtes connecter")

            # TODO ici les verification
            # if True:
            #     ...
            login(request,user)
            if user.is_staff:
                return redirect("/admin")
            return redirect(reverse("profile_candidat"))
        else:
            return render(request, "registration/login.html", context={"error": "Utilisateur nom trouvé"})


    return render(request, "registration/login.html")


def my_inscription(request):

    # TODO vers la page correspondante
    if request.user.is_staff:
        return redirect("/admin")

    if request.user.is_authenticated:
        if True:
            return render(request, "emploi/profile_candidat.html")

    if request.method == "POST":
        post = request.POST
        nom = post.get("nom")
        prenom = post.get("prenom")
        numero = post.get("numero")
        email = post.get("email")
        username = post.get("username")
        password = post.get("password")
        password1 = post.get("password1")
        quartier = post.get("quartier")
        sexe = post.get("sexe")

        if password1 != password:
            return render(request, "registration/inscription.html",
                          context={"error": "Les mots de passe sont différents"})

        Utilisateur.objects.create_user(username=username,password=password, email=email, last_name=nom, first_name=prenom, numero=numero,
                                        quartier=quartier, sexe=sexe, type_compte="candidat")
        logout(request)
        messages.success(request, "Merci de vous avoir inscrit sur notre site")
        return redirect(reverse("profile_candidat"))

    return render(request, "registration/inscription.html")


def my_logout(request):
    logout(request)
    messages.success(request,"Vous êtes déconnecter")
    return redirect(reverse("my_login"))


def mot_de_passe_oublier(request):
    return render(request, "registration/mot_de_pass_oublier.html")
