# complexité == efficacité
# efficacité :
# - temps d'exécution
# - espace mémoire

# notation de Landau : O() (lettre O, pas le chiffre 0)
# pas une fonction mais un ensemble

# O(c) (c == constante)
# O(1)
result = 123 + 42
print(result)


# recherche par dicothomie
# recherche d'un fruit dont la lettre démarre par une lettre
# O(log(n))
# log == logarithme naturel
words = ['ananas', 'banane', 'cerise', 'durian', 'kiwi', 'orange', 'pomme']

# O(n)
# n est la quantité de données à traiter
numbers = [123, 42, 3.14]

for number in numbers:
    result = number * 2
    print(result)

# recherche par dicothomie dans une liste
# O(n * log(n))
my_list = [
    ['ananas', 'banane', 'cerise', 'durian', 'kiwi', 'orange', 'pomme'],
    [0, 1, 2, 3, 3.14, 42, 53, 123, 999]
]

# O(n * m) == O(n * n) == O(n²)
# n est la quantité de données à traiter de la première liste
# m est la quantité de données à traiter de la deuxième liste
numbers = [123, 42, 3.14]
more_numbers = [2.71, 3.14, 0, 53]
common_numbers = []

for number in numbers:
    for more_number in more_numbers:
        if number == more_number:
            common_numbers.append(number)

# O(n * n) == O(n²)
matrix = [
    [123, 42, 3.14],
    [2.71, 3.14, 0],
    [1, 2, 3]
]

for line in matrix:
    for number in line:
        result = number * 2
        print(result)

# O(n * n * n) == O(n³)
cube = [
    [
        ['a1', 'a2', 'a3'],
        ['a4', 'a5', 'a6'],
        ['a7', 'a8', 'a9'],
    ],
    [
        ['b1', 'b2', 'b3'],
        ['b4', 'b5', 'b6'],
        ['b7', 'b8', 'b9'],
    ],
    [
        ['c1', 'c2', 'c3'],
        ['c4', 'c5', 'c6'],
        ['c7', 'c8', 'c9'],
    ]
]

for square in cube:
    for line in square:
        for spot in line:
            print(spot)

# Algorithmes pas efficaces du tout
# O(n ** n)
# O(n!) == O(n * (n - 1) * (n - 2) * ... * 2)
# 5! == 5 * 4 * 3 * 2

# exo 1 : déterminez la complexité algorithmique de ce programme
# O(?)
numbers = [4, 10, 42, 3.14]
my_list = []

while True:
    number = numbers.pop()
    my_list.append(number)

    if len(numbers) == 0:
        break

# exo 2 : déterminez la complexité algorithmique de ce programme
# O(?)
numbers = [4, 10, 42, 3.14]
my_list = []

for n in numbers:
    # puissance 2
    result = n ** 2
    my_list.append(result)
