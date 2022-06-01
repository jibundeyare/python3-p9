# 2. Carré formé de deux nombres consécutifs

# 183 184 est le carré a six chiffres de 428. On remarque que ses trois
# premiers chiffres et ses trois derniers forment deux nombres consécutifs
# 183 et 184.
# Trouver 1'unique carré a huit chiffres tel que ses quatre premiers
# chiffres et ses quatre derniers représentent deux nombres consécutifs.

# for i in range(1000, 10000 + 1):
#     print(i, i ** 2)

# limite inférieure
# 3163 * 3163 = 10004569
# limite supérieure
# 9999 * 9999 = 99980001

for i in range(1000, 9999 + 1):
    carre = i ** 2

    premier_nombre = carre // 10000
    dernier_nombre = carre % 10000

    # @debug
    # print(carre, premier_nombre, dernier_nombre)

    if dernier_nombre - premier_nombre == 1:
        print(i, carre, premier_nombre, dernier_nombre)
