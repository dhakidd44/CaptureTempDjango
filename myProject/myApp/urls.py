from django.urls import path
from . import views

urlpatterns = [
    path("", views.lire_et_enregistrer, name="lire_et_enregistrer")
]