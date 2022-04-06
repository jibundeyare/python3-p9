# 1. Trois carrés pour le prix d'un

# 49 est un carré à deux chiffres. Si on le découpe en deux nombres
# 4 et 9, on obtient deux carrés à un chiffre. 49 est le seul carré a deux
# chiffres possédant cette particularité.
# Trouver 1'unique carré à quatre chiffres tel que ses deux premiers
# chiffres et ses deux derniers représentent deux carrés à deux chiffres.

from timeit import default_timer as timer

# start benchmark
start = timer()

for _ in range(0, 100000):
    # la liste qui contiendra nos réponses
    resultats = []

    # carré de 2 chiffres : 4 à 9
    carres_2_chiffres = []

    for i in range(4, 10):
        carres_2_chiffres.append(i ** 2)

    # @debug
    # print(carres_2_chiffres)

    # carré de 4 chiffres : 32 à 99
    carres_4_chiffres = []

    for i in range(32, 100):
        carres_4_chiffres.append(i ** 2)

    # @debug
    # print(carres_4_chiffres)

    # construisons des nombres à 4 chiffres
    for i in carres_2_chiffres:
        for j in carres_2_chiffres:
            nombre = i * 100 + j

            if nombre in carres_4_chiffres:
                resultats.append(nombre)

print(resultats)

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# [1681]
# duration: 9.564540112000032
