# 17. Cryptarithme
#
# Un cryptarithme est une opération dans laquelle chaque
# chiffre a été remplacé par une lettre. Une même lettre représente tou-
# jours le même chiffre, deux lettres différentes représentent deux chiffres
# différents et aucun nombre ne peut commencer par un zéro. La figure 7
# montre un exemple de cryptarithme.
#
#   NEUF
# +   UN
# +   UN
# ------
#   ONZE
#
# Figure 7 - Cryptarithme
#
# À partir de cette addition en lettres, retrouver celle en chiffres.

# lettres : n, e, u, f, o, z
# nombre de lettres : 6
# nombre maximum d'opérations nécessaires pour trouver le résultat :
# 10 * 9 * 8 * 7 * 6 * 5 = 151200
# nombre exacte d'opérations nécessaires pour trouver le résultat :
# 9 * 8 * 7 * 7 * 6 * 5 = 105840

i = 0

for n in range(1, 10):
    for e in range(0, 10):
        if e == n:
            continue

        for u in range(1, 10):
            if u == n or u == e:
                continue

            for f in range(0, 10):
                if f == n or f == e or f == u:
                    continue

                for o in range(1, 10):
                    if o == n or o == e or o == u or o == f:
                        continue

                    for z in range(0, 10):
                        if z == n or z == e or z == u or z == f or z == o:
                            continue

                        neuf = n * 1000 + e * 100 + u * 10 + f
                        un = u * 10 + n
                        onze = o * 1000 + n * 100 + z * 10 + e

                        if neuf + un + un == onze:
                            print('n e u f o z:', n, e, u, f, o, z)

                        i += 1

print('i:', i)

