from vehicule import Vehicule

class Camion(Vehicule):
    """
    Cette classe représente un camion.
    """

    # redéfinir une méthode (fonction) d'une classe mère dans une classe enfant s'appelle "surcharger une méthode"
    def __init__(self, marque: str, modele: str, carburant: str, vitesse: int, ptac: float):
        super().__init__(marque, modele, carburant, vitesse)
        # il faut utiliser le setter s'il y a une procédure de vérification des données avant l'affectation
        self.set_ptac(ptac)

    # redéfinir une méthode (fonction) d'une classe mère dans une classe enfant s'appelle "surcharger une méthode"
    def __str__(self):
        return super().__str__() + f" {self._ptac}"

    def get_ptac(self) -> float:
        return self._ptac

    def set_ptac(self, ptac: float):
        if type(ptac) != float:
            raise Exception("Le ptac doit être un float")

        self._ptac = ptac
