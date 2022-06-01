data = [5, 3.14, 42, 1]

while True:
    moved = False

    for i in range(0, len(data) - 1):
        a = data[i]
        b = data[i + 1]

        if a > b:
            # on interchange l'élément actuel et le suivant
            data[i], data[i + 1] = data[i + 1], data[i]
            moved = True

    if moved == False:
        break

print(data)
