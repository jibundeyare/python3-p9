class Chaise:
    # variable de classe
    nombre_pieds = 4

    def __init__(self, couleur: str):
        # variable d'instance
        self.couleur = couleur

    # getter de variable d'instance
    def get_couleur(self) -> str:
        return self.couleur

    # setter de variable d'instance
    def set_couleur(self, couleur: str):
        self.couleur = couleur

    # getter de variable de classe
    @classmethod
    def get_nombre_pieds(cls):
        return cls.nombre_pieds

    # setter de variable de classe
    @classmethod
    def set_nombre_pieds(cls, nombre_pieds: int):
        cls.nombre_pieds = nombre_pieds

# instanciation
chaise1 = Chaise('noir')
chaise2 = Chaise('noir')

# modif d'une variable d'instance
chaise1.couleur = 'blanc'

# modif d'une variable de classe
Chaise.nombre_pieds = 3

# modif d'une variable de classe (même effet qu'au dessus)
chaise1.set_nombre_pieds(1)

# attention : ceci n'est pas une modif de variable de classe
# création d'une variable d'instance qui fait de l'ombre à la variable de classe
chaise1.nombre_pieds = 5

# lecture d'une variable de classe
print('Chaise.nombre_pieds:', Chaise.nombre_pieds)

# lecture d'une variable de classe (même effet qu'au dessus)
print('chaise1.get_nombre_pieds:', chaise1.get_nombre_pieds())

# lecture d'une variable d'instance si elle existe
# sinon lecture d'une variable de classe
print('chaise1.nombre_pieds:', chaise1.nombre_pieds)
# lecture d'une variable d'instance
print('chaise1.couleur:', chaise1.couleur)

# lecture d'une variable d'instance si elle existe
# sinon lecture d'une variable de classe
print('chaise2.nombre_pieds:', chaise2.nombre_pieds)
# lecture d'une variable d'instance
print('chaise2.couleur:', chaise2.couleur)
