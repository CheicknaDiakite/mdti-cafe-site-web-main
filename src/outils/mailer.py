
from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER

"""
Pour envoyer des email
email_liste est une liste ou un tuple
"""
def send(sujet="pas de sujet",message="pas de message",email_liste=""):
    try:
        send_mail(
            sujet,
            message,
            EMAIL_HOST_USER
            ,
            email_liste,
        )

        return True
    except :
        return False

