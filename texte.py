import random

firstname = "toto"
lastname = "pop"
number = random.randint(2, 10)

email = firstname + '.' + lastname + str(number) + '@example.com'
print(email)

new_emails = random.randint(0, 3)

if new_emails == 0:
    print("Vous n'avez pas de nouveaux mails")
elif new_emails == 1:
    print("Vous avez reçu <strong>1</strong> nouveau mail" )
else:
    print("Vous avez reçu <strong>" + str(new_emails) + "</strong> nouveaux mails" )

stock = random.randint(0, 15)

if stock == 0:
    print("Stock épuisé")
elif stock == 1:
    print("Stock en tension : 1 pièce")
elif 1 < stock < 5:
    print(f"Stock en tension : {stock} pièces")
elif 5 <= stock < 10:
    print(f"Stock confortable : {stock} pièces")
elif 10 <= stock:
    print(f"Stock en surnombre : {stock} pièces")

temperature = 10.1 + 0.1 + 0.1
print(temperature)

print(f"La température actuelle est de {temperature:.2f}° C")

electricite = True

# ne pas faire d'interpolation de variable booléenne si votre appli n'est pas en anglais
if electricite:
    print('electricite: vrai')
else:
    print('electricite: faux')

print(f"le nombre tiré au hasard est : {random.randint(0, 10)}")
#        0123456789A
texte = "foo bar baz"
# len == length == longueur
print(len(texte))

# find() -> int
# find() -> int >= 0 si le texte est trouvé
# find() -> int == -1 si le texte n'est pas trouvé

print(texte.find("ba"))
# recherche à partir du caractère 5 inclus
print(texte.find("ba", 5))
print(texte.find("banana"))

texte = "Bonjour Toto"

# rédiger un bloc if qui indique si le keyword est présent ou non dans la chaîne de caractères
# affichez "trouvé" si le keyword est présent
# sinon affichez "non trouvé"
keyword = "Toto"

# rédiger un bloc if qui indique si le keyword est présent ou non dans la chaîne de caractères
# affichez "trouvé" si le keyword est présent
# sinon affichez "non trouvé"
keyword = "Titi"

# remplacement
texte = "Bnjour  Toto"
texte = texte.replace('Bnjour', 'Bonjour')
texte = texte.replace('  ', ' ')
texte = texte.replace('Toto', 'Titi')
print(texte)
