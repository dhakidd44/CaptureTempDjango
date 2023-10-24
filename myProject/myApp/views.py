from django.shortcuts import render
from .models import DonneeCapteur
import serial
# Create your views here.
def lire_et_enregistrer(request):
    context ={}
    try:
        port = serial.Serial('/dev/ttyACM0', 9600)  # Assurez-vous d'ajuster le port série selon votre configuration
        donnees = port.readline()
        donnees = float(donnees.decode().strip())  # Convertir les données en float
        port.close()
        
        # Enregistrez les données dans la base de données
        donnee_capteur = DonneeCapteur(temperature=donnees)
        donnee_capteur.save()

        return render(request, "myApp/index.html", context)
    except serial.SerialException:
        return render("Erreur de communication avec l'Arduino")