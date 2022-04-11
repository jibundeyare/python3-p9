from voiture import Voiture

v1 = Voiture("BMW", "Série 5", "diesel", "berline", 0)
# v1 affiche "<voiture.Voiture object at 0x7fef1ecfc910>" si la fonction __str__() n'a pas été définie
print(v1)
# Il ne faut pas afficher directement ces variables car elles sont considérées comme si elles étaient privées.
# C-à-d qu'ellesd sont toutes préfixées d'un underscore "_".
# print(v1.marque, v1.modele, v1.carburant, v1.type_carrosserie, v1.get_vitesse())

print(v1.get_vitesse())
v1.set_vitesse(10)
print(v1.get_vitesse())

v2 = Voiture("Ford", "Mustang 68", "essence", "muscle car", "nimp")
print(v2)
print(v2.get_vitesse())
# transmettre une valeur de type autre que int génère l'erreur "Exception: La vitesse doit être un nombre entier"
v2.set_vitesse(50)
print(v2.get_vitesse())
print(v1.get_vitesse())
