text = "foo bar baz"
splitted_text = text.split(' ')

print(splitted_text)
print(len(splitted_text))
result = splitted_text[0]
splitted_text[0] = 'toto'
# print(result)
print(splitted_text)
print(splitted_text[1])
print(splitted_text[2])
# print(splitted_text[3]) # erreur
# splitted_text[3] = 123 # erreur

index = 0
splitted_text[index] = 42
splitted_text[index + 1] = 123

# interversion de valeur dans une liste (version python)
splitted_text[index], splitted_text[index + 1] = splitted_text[index + 1], splitted_text[index]

# interversion de valeur dans une liste (version plus classique)
tmp = splitted_text[index]
splitted_text[index] = splitted_text[index + 1]
splitted_text[index + 1] = tmp

splitted_text.append(123)
print(splitted_text)

# help(splitted_text.append)

# [start:end:step]
# start inclus
# end exclus

start = 0
end = 2
step = 0
result = splitted_text[start:end:step+1]
print(result)

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris quis aliquam orci. Aliquam pellentesque odio eu lacus mollis dictum a at nisl. Suspendisse nec eros et velit feugiat gravida. Pellentesque tempor odio vel nisl hendrerit lobortis. Etiam in consequat sem, a malesuada ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis posuere rhoncus tempor. Nulla dapibus condimentum lorem non ullamcorper. Aenean congue, libero vel ultrices luctus, lectus libero scelerisque purus, vitae interdum lacus risus sed ligula. Aliquam erat volutpat. Praesent fringilla, tellus at consectetur fringilla, mauris massa tristique ligula, non mollis lorem felis non elit. Curabitur placerat orci in nisl varius, convallis sollicitudin enim aliquet. Nam quis leo eget leo posuere tincidunt."

# suppression des virgules (remplacement par une chaîne de caractères vide)
text = text.replace(',', '')
# suppression des points (remplacement par une chaîne de caractères vide)
text = text.replace('.', '')

# suppression des virgules (remplacement par une chaîne de caractères vide)
splitted_text = text.split(',')
text = ''.join(splitted_text)
# suppression des points (remplacement par une chaîne de caractères vide)
splitted_text = text.split('.')
text = ''.join(splitted_text)

splitted_text = text.split(' ')
print(len(splitted_text))

# tous les mots de l'index 3 inclus à l'index 7 exclus
partial_list = splitted_text[3:7]

# tous les mots de l'index 3 inclus à l'index 7 exclus avec un pas de 2
partial_list = splitted_text[3:7:2]

# ATTENTION ne fonctionne pas dans l'autre sens
# tous les mots de l'index 7 inclus à l'index 3 exclus
# l'index start doit être strictement inférieur à l'index end
partial_list = splitted_text[7:3]
print(partial_list)
print(splitted_text)

start = 7
end = 3

if start >= end:
    start, end = end, start

print(start, end)
partial_list = splitted_text[start:end]

partial_list = splitted_text[-7:-3]

partial_list = splitted_text[-7:-3:2]

print(splitted_text)
print(partial_list)

# exo
# 1. Récupérez dans splitted_text les mots de l'index 35 à 49 inclus
start = 35
end = 49
result = splitted_text[start:end+1]

start = 35
end = 49+1 # 50
result = splitted_text[start:end]

# 2. Affichez le numéro du dernier index
# dernier_index = taille_liste -1
dernier_index = len(splitted_text) - 1

# 3. Récupérez 1 mot sur 2 de l'index 0 au dernier index
# ATTENTION utilisez le dernier index calculé dans l'étape 2
result = splitted_text[0:dernier_index+1:2]

taille_liste = len(splitted_text)
result = splitted_text[0:taille_liste:2]

# 4. créez trois listes contenant :
# - le premier mot sur trois
# - le deuxième mot sur trois
# - le troisième mot sur trois
#
# Exemple :
# liste_originale = ['foo', 'bar', 'baz', 'lorem', 'ipsum']
# liste_partielle1 == ['foo', 'lorem']
# liste_partielle2 == ['bar', 'ipsum']
# liste_partielle3 == ['baz']
liste1 = splitted_text[0:dernier_index+1:3]
liste2 = splitted_text[1:dernier_index+1:3]
liste3 = splitted_text[2:dernier_index+1:3]

# copie de tous les éléments
# valeurs par défaut :
# - start = 0
# - end = len()
# - step = 1
result = splitted_text[::]

# copie de tous les éléments en ordre inverse
result = splitted_text[::-1]

# copie de tous les éléments à partir de start jusqu'à la fin
start = 3
result = splitted_text[start:]

# copie de tous les éléments du début jusqu'à end
end = 10
result = splitted_text[:end]

my_list = []
my_list.append("foo")
my_list.append(123)
my_list.append(3.14)
