from timeit import default_timer as timer

# start benchmark
start = timer()

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

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)

# [1681]
# duration: 0.00019438199979049386
