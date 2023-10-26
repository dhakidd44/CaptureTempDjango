from django.shortcuts import render, HttpResponse
from .models import DonneeCapteur
import serial
import json

def afficher_graphique(request):
    # Lire les données de l'Arduino et les stocker dans la base de données
    try:
        port = serial.Serial('COM7', 9600)  # Assurez-vous d'ajuster le port série selon votre configuration
        donnees = port.readline()
        donnees = float(donnees.decode().strip())  # Convertir les données en float
        port.close()
        
        # Enregistrez les données dans la base de données
        donnee_capteur = DonneeCapteur(temperature=donnees)
        donnee_capteur.save()
    except serial.SerialException:
        return HttpResponse("Erreur de communication avec l'Arduino")

    # Récupérer les dernières données depuis la base de données
    donnees = DonneeCapteur.objects.all().order_by('-timestamp')[:10000]
    labels = [str(d.timestamp) for d in donnees]
    valeurs = [d.temperature for d in donnees]

    # Utilisez json.dumps() pour formater les données correctement
    labels_json = json.dumps(labels)
    valeurs_json = json.dumps(valeurs)

    context = {
        'labels_json': labels_json,
        'valeurs_json': valeurs_json,
    }

    return render(request, "myApp/graphique.html", context)