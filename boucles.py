import random

# les types de boucle :
# - while
# - do while
# - for classique
# - for each

# reproduction d'une boucle for classique avec une boucle while
# condition d'initialisation
counter = 0
# taille de la boucle
limit = 10

# condition de continuation
while counter < limit:
    # action à répéter
    print("for classique:", counter)

    # incrément / décrement
    counter += 1

# reproduction d'une boucle do while avec une boucle while
# condition d'initialisation
counter = 0
# taille de la boucle
limit = 10

while True:
    # action à répéter
    print("do while:", counter)

    # incrément / décrement
    counter += 1

    # condition de continuation
    if not (counter < limit):
        break

# for de python
for counter in range(0, 10):
    # action à répéter
    print('for python:', counter)

# for de python
mots = ['foo', 'bar', 'baz']

# ATTENTION méthode non recommandée pour boucler sur tous les éléments d'une liste
for i in range(0, len(mots)):
    # action à répéter
    print(f"mot (non reco) {i}:", mots[i])

# méthode recommandée pour boucler sur tous les éléments d'une liste
for mot in mots:
    # action à répéter
    print("mot (reco):", mot)

for i, mot in enumerate(mots):
    # action à répéter
    print(f"mot (reco) {i}:", mot)

# affichage des nombres de 0 à 10 avec un "pas" (step) de 2
for i in range(0, 10, 2):
    print(i)

# exo : affichez les nombres de 100 à 999 inclus avec une boucle for
start = 100
end = 999
for i in range(start, end + 1):
    print(i)

# exo : affichez les nombres de 0 à 20 inclus qui sont multiples de 3
start = 0
end = 20
step = 3
for i in range(start, end + 1, step):
    print(i)

# exo : même question mais avec une autre méthode
start = 0
end = 20
for i in range(start, end + 1):
    if i % 3 == 0:
        print(i)

# exo : affichez les nombres de 10 à 1 inclus à rebours
# info : la fonction range() prend un troisième paramètre qui indique le "pas" (step)

# algo : tirage de 2 nombres différents parmi 5
numbers = []

# 1er tirage
n = random.randint(1, 5)
numbers.append(n)

# 2ème tirage
while True:
    n = random.randint(1, 5)

    # condition d'arrêt
    if n not in numbers:
        # le nombre n'a pas encore été tiré au hasard
        # on peut sortir de la boucle
        break

numbers.append(n)
print(numbers)
