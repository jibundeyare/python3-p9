from voiture import Voiture
from camion import Camion

c1 = Camion("Scania", "?", "diesel", 100, 19.0)
print(c1)
c2 = Camion("Mercedes", "?", "diesel", 0, 19.0)
print(c2)

v1 = Voiture("BMW", "Série 5", "diesel", 0, "berline")
# v1 affiche "<voiture.Voiture object at 0x7fef1ecfc910>" si la fonction __str__() n'a pas été définie
print(v1)
# Il ne faut pas afficher directement ces variables car elles sont considérées comme si elles étaient privées.
# C-à-d qu'ellesd sont toutes préfixées d'un underscore "_".
# print(v1.marque, v1.modele, v1.carburant, v1.type_carrosserie, v1.get_vitesse())
print(v1.get_marque())
print(v1.get_modele())
print(v1.get_carburant())
print(v1.get_type_carrosserie())

print(v1.get_vitesse())
v1.set_vitesse(10)
print(v1.get_vitesse())

v2 = Voiture("Ford", "Mustang 68", "essence", 0, "muscle car")
print(v2)
print(v2.get_vitesse())
# transmettre une valeur de type autre que int génère l'erreur "Exception: La vitesse doit être un nombre entier"
v2.set_vitesse(50)
print(v2.get_vitesse())
print(v1.get_vitesse())

my_list = []
my_list.append(v1)
my_list.append(v2)
my_list.append(c1)
my_list.append(c2)

for item in my_list:
    print(item._marque)
    print(item.get_vitesse())
    if type(item) is Voiture:
        # code spécifique aux voitures
        print(item._type_carrosserie)
        print(item.get_type_carrosserie())

    if type(item) is Camion:
        # code spécifique aux camions
        print(item._ptac)
        print(item.get_ptac())

for i in range(0, len(my_list)):
    print(my_list[i]._marque)
    print(my_list[i].get_vitesse())
