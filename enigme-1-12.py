# Un artilleur dispose de boulets de canon répartis dans un carré parfait. Pour réduire l'encombrement au sol, l'artilleur réussit à empiler ses boulets pour former une belle pyramide à base carrée.
# Quel est le plus petit nombre de boulets possible dont dispose l'artilleur ?

# Complexité algorithmique
# O(n + n²) == O(n * (1 + n))

# On démarre à 2 pour éviter que la boucle for principale
# trouve 1 comme résultat.
# De plus ça nous évite de faire un if à chaque itération qui
# vérifie que le résultat est différent de 1.
# liste en compréhension
squares = [i ** 2 for i in range(2, 101)]

# fait la même chose avec une boucle for
# squares = []
# for i in range(1, 101):
#     squares.append(i ** 2)

# Comme les carrés précalculés démarrent à 1, il faut pré-compter
# ce boulet dans la pyramide.
pyramid = 1

for bullet in squares:
    pyramid += bullet

    if pyramid in squares:
        print(pyramid)
        break
