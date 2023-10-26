from django.urls import path
from . import views

urlpatterns = [
    path("", views.afficher_graphique, name="afficher_graphique"),
]