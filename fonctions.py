def int_average(numbers: list) -> int:
    """
    Cette fonction renvoie un arrondi de la moyenne des nombres passés en
    paramètres.

    numbers: list Cette liste contient les nombres (int ou float) dont il faut calculer la moyenne.
    return: int La fonction renvoie une moyenne arrondie au format int.
    """

    # le nombre d'éléments
    n = len(numbers)

    # existe mais pas pédagogique !
    # total = sum(numbers)

    # initialisation de l'accumulateur
    total = 0

    for number in numbers:
        total += number

    # moyenne = total / nombre d'éléments
    average = total / n

    # arrondi du résultat
    average = round(average)

    return average

# le scores de 5 joueurs
scores = [433, 562, 574, 800, 953]
average = int_average(scores)

# le scores de 5 joueurs
scores = [302, 102, 956, 987, 931]
average = int_average(scores)
print(average)
