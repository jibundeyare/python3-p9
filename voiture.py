from vehicule import Vehicule

class Voiture(Vehicule):
    """
    Cette classe représente une voiture.
    C'est une classe concrète qui étend (ou hérite de) la classe Vehicule.
    Cette classe est destinée à être instanciée.
    """

    def __init__(self, marque: str, modele: str, carburant: str, vitesse: int, type_carrosserie: str):
        super().__init__(marque, modele, carburant, vitesse)
        self._type_carrosserie = type_carrosserie

    def __str__(self):
        return super().__str__() + f" {self._type_carrosserie}"

    def get_type_carrosserie(self) -> str:
        return self._type_carrosserie
