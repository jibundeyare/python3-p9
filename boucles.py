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
