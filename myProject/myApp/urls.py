from django.urls import path
from . import views

urlpatterns = [
    path("", views.lire_et_enregistrer, name="lire_et_enregistrer"),
    path("", views.afficher_graphique, name="afficher_graphique")
]