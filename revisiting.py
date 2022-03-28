import random

# Exo 1.1
# Affichez le type de donnée des variables a et b.

a = 3.14
b = 3

# Réponse 1.1
print(type(a))
print(type(b))

# Exo 1.2
# En utilisant les variables a et b, affichez les chiffres après la virgule de la variable a. Le résulta attendu est 0.14.

a = 3.14
b = 3

# Réponse 1.2
print(a - b)

# Exo 1.3
# Affichez le type de données de la variable n.

n = random.randint(10, 99) / 10

# Réponse 1.3
print(type(n))

# Exo 1.4
# Convertissez n en un nombre entier, stockez le résultat dans une variable et affichez le résultat.

n = random.randint(10, 99) / 10

# Réponse 1.4
n = int(n)
print(n)

# Exo 1.5
# Affichez :
# - les nombres avant la virgule de la variable n
# - les nombres après la virgule de la variable n
#
# Avec n = 8.5, le résulta attendu est 8 et 0.5.

n = random.randint(10, 99) / 10
print(n)

# Réponse 1.5
n_integer = int(n)
print(n_integer)
print(n - n_integer)

# Exo 1.6
# Stockez dans une variable si la variable n est "mathématiquement" un nombre entier ou non.

n = random.randint(10, 99) / 10
print(n)

# Réponse 1.6

# Exo 2.1
# Affichez le texte "foo", si la variable n est inférieure à 5.

n = random.randint(0, 9)
print(n)

# Réponse 2.1
if n < 5:
    print("foo")

# Exo 2.2
# Tirez un nombre au hasard compris entre 0 et 9 inclus sans le stocker dans une variable et affichez le texte "foo", si le nombre est inférieure à 5.
# Vous pouvez utiliser random.randint(0, 9) pour tirer le nombre au hasard.

# Réponse 2.2
if random.randint(0, 9) < 5:
    print("foo")

# Exo 2.3
# Affichez le texte "foo" tant que vous tirez au hasard un nombre compris entre 0 et 9 inclus, strictement plus petit que 5.
# Vous pouvez utiliser random.randint(0, 9) pour tirer le nombre au hasard.

# Réponse 2.3
while True:
    pass
