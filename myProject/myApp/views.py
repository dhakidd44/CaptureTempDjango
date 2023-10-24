from django.shortcuts import render, HttpResponse
from myApp.models import DonneeCapteur
import serial
# Create your views here.
def lire_et_enregistrer(request):
    try:
        port = serial.Serial('COM9', 9600)  # Assurez-vous d'ajuster le port série selon votre configuration
        donnees = port.readline()
        donnees = float(donnees.decode().strip())  # Convertir les données en float
        port.close()
        
        # Enregistrez les données dans la base de données
        donnee_capteur = DonneeCapteur(temperature=donnees)
        donnee_capteur.save()

        context ={'donnees': donnees}
        return render(request, "myApp/index.html", context)
    except serial.SerialException:
        return HttpResponse("Erreur de communication avec l'Arduino")
    
def afficher_graphique(request):
    donnees = DonneeCapteur.objects.all()[:10000]
    labels = [str(d.timestamp) for d in donnees]
    valeurs = [d.temperature for d in donnees]

    context = {
        'labels': labels,
        'valeurs': valeurs,
    }
    return render(request, "myApp/graphique.html", context)
