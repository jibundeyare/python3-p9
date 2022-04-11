class Camion:
    """
    Cette classe représente un camion.
    """
    def __init__(self, marque: str, modele: str, carburant: str, type_carrosserie: str, vitesse: int):
        self._marque = marque
        self._modele = modele
        self._carburant = carburant
        self._type_carrosserie = type_carrosserie
        # il faut utiliser le setter s'il y a une procédure de vérification des données avant l'affectation
        self.set_vitesse(vitesse)

    # getter
    def get_vitesse(self) -> int:
        return self._vitesse

    # setter
    def set_vitesse(self, vitesse: int):
        if type(vitesse) is not int:
            raise Exception("La vitesse doit être un int")
        elif vitesse > 220:
            raise Exception("La vitesse max est de 220")
        elif vitesse < -10:
            raise Exception("La vitesse min est de -10")

        self._vitesse = vitesse

    def accelerer(self):
        vitesse = self.get_vitesse()
        vitesse += 10
        self.set_vitesse(vitesse)

    def ralentir(self):
        vitesse = self.get_vitesse()
        vitesse -= 10
        self.set_vitesse(vitesse)
