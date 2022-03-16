# + - * /
result = 123 + 4.14
print(result)

# ()
result = (1 + 2) * 3
print(result)

# // % **
# division entière
result = 1 // 3
print(result)

# modulo
result = 10 % 3
print(result)

# vérification de la divisibilité
result = 7685923 % 7
print(result)

# puissance
# dans certains langages c'est : ^, pow()
result = 3 ** 2
print(result)

# racine carrée
result = 3 ** (1 / 2)
print(result)

# racine cubique
result = 3 ** (1 / 3)
print(result)

# opérateur booléen "and"
result = True and True # True
result = False and True # False
result = True and False # False
result = False and False # False

# s'il n'y a que des "and", l'ordre n'est pas important
result = True and False and True and False # False

# opérateur booléen "or"
result = True or True # True
result = False or True # True
result = True or False # True
result = False or False # False

# s'il n'y a que des "or", l'ordre n'est pas important
result = True or False or True or False # True

result = not False
print(result)

# opérateur de négation "not"
is_user_majeur = True
result = not is_user_majeur
# éqauivalent à
# result = is_user_majeur == False

# opérateur booléen "xor", le "ou exclusif"
result = True ^ True # False
result = False ^ True # True
result = True ^ False # True
result = False ^ False # False

# opérateurs composés

# n'existe pas en python
# c++ <=> c = c + 1

number = 42
# number = number + 1
n = 1
number += n

# == != < > <= >=

a = 123
b = 42

# égal
result = a == b
print(result)

# différent
result = a != b
print(result)

# inférieur ou égal
result = a <= b
print(result)

# l'opérateur == fait office de comparaison d'identité
a = "123"
b = 123
result = a == b
print(result)

# pas en python
# === !==

fruits = ["apple", "banana", "cherry"]
result = "banana" in fruits
print(result)

result = "orange" in fruits
print(result)

result = type(123) is float
print(result)

# encadrement
import random

a = 42
b = 123

c = random.randint(1, 150)

result = a < 50 < b
print(result)

result = a < c < b
print(c)
print(result)
