import random

# if True:
#     print("ce message sera toujours affiché")

# if False:
#     print("ce message ne sera jamais affiché")

# if True:
#     print("ce message sera toujours affiché (if True)")
# else:
#     print("ce message ne sera jamais affiché (if True)")

# if False:
#     print("ce message ne sera jamais affiché (if False)")
# else:
#     print("ce message sera toujours affiché (if False)")

# fruits = ['apples', 'bananas', 'cherries']

# if 'apples' in fruits:
#     print("Il y a des pommes")
# else:
#     print("Il n'y a pas de pommes")

# if 'oranges' in fruits:
#     print("Il y a des oranges")
# else:
#     print("Il n'y a pas d'oranges")

# is_authenticated = True

# if is_authenticated:
#     print("L'utilisateur peut accéder aux backoffice")

# user_password_in_db = "abc"
# user_password_in_form = "123"

# if user_password_in_form == user_password_in_db:
#     print("L'utilisateur peut accéder aux backoffice")
# else:
#     print("Le login ou le mot de passe est incorrect")

# users_in_db = ['toto', 'titi', 'tata', 'tutu']
# tutu_password_in_db = 'abc'

# user_name_in_form = 'tutu'
# user_password_in_form = 'abc'

# if user_name_in_form in users_in_db and user_password_in_form == tutu_password_in_db:
#     print("L'utilisateur peut accéder aux backoffice")
# else:
#     print("Le login ou le mot de passe est incorrect")

# is_authenticated = True
# users_in_db = ['toto', 'titi', 'tata', 'tutu']
# tutu_password_in_db = 'abc'

# user_name_in_form = 'tutu'
# user_password_in_form = '123'

# if is_authenticated or (user_name_in_form in users_in_db and user_password_in_form == tutu_password_in_db):
#     print("L'utilisateur peut accéder aux backoffice")
# else:
#     print("Le login ou le mot de passe est incorrect")

# electricity_is_off = bool(random.randint(0, 1))
# water_is_off = bool(random.randint(0, 1))
# gas_is_off = bool(random.randint(0, 1))

# print('electricity_is_off:', electricity_is_off)
# print('water_is_off:', water_is_off)
# print('gas_is_off:', gas_is_off)

# # vérifiez que toutes les sources sont coupées
# # si c'est le cas, affichez le message "Vous pouvez partir en we"
# # sinon, affichez le message "Il reste des sources à couper"

# if electricity_is_off and water_is_off and gas_is_off:
#     print("Vous pouvez partir en we")
# else:
#     print("Il reste des sources à couper")

#     if not electricity_is_off:
#         print("Coupez l'électricité")

#     if not water_is_off:
#         print("Coupez l'eau")

#     if not gas_is_off:
#         print("Coupez le gaz")

# electricity_is_on = bool(random.randint(0, 1))
# water_is_on = bool(random.randint(0, 1))
# gas_is_on = bool(random.randint(0, 1))

# print('electricity_is_on:', electricity_is_on)
# print('water_is_on:', water_is_on)
# print('gas_is_on:', gas_is_on)

# # vérifiez que toutes les sources sont coupées
# # si c'est le cas, affichez le message "Vous pouvez partir en we"
# # sinon, affichez le message "Il reste des sources à couper"

# if not electricity_is_on and not water_is_on and not gas_is_on:
#     print("Vous pouvez partir en we")
# else:
#     print("Il reste des sources à couper")

#     if electricity_is_on:
#         print("Coupez l'électricité")
    
#     if water_is_on:
#         print("Coupez l'eau")

#     if gas_is_on:
#         print("Coupez le gaz")

# has_cash = bool(random.randint(0, 1))
# has_card = bool(random.randint(0, 1))
# has_check = bool(random.randint(0, 1))

# print('has_cash:', has_cash)
# print('has_card:', has_card)
# print('has_check:', has_check)

# # vérifiez qu'au moins un moyen de paiement est disponible
# # si c'est le cas, affichez le message "Vous pouvez partir faire les courses"
# # sinon, affichez le message "Vous n'avez aucun moyen de paiement"

# if has_cash or has_card or has_check:
#     print("Vous pouvez partir faire les courses")

#     if has_cash:
#         print("Vous avez du liquide")

#     if has_card:
#         print("Vous avez une carte bancaire")

#     if has_check:
#         print("Vous avez un chéquier")
# else:
#     print("Vous n'avez aucun moyen de paiement")

age = random.randint(0, 100)

# 0-5 bébé
# 6-11 enfant
# 12-25 ado, jeune adulte
# 26-59 adulte
# 60+ senior

if age <= 5:
    print('bébé')
elif 6 <= age <= 11:
    print('enfant')
elif 12 <= age <= 25:
    print('ado, jeune adulte')
elif 26 <= age <= 59:
    print('adulte')
# on peut aussi faire un "else" pour intercepter les cas où l'âge >= 60
elif age >= 60:
    print('senior')

if age <= 5:
    print('bébé')
else:
    if 6 <= age <= 11:
        print('enfant')
    else:
        if 12 <= age <= 25:
            print('ado, jeune adulte')
        else:
            if 26 <= age <= 59:
                print('adulte')
            else:
                if age >= 60:
                    print('senior')

if 123:
    # le message s'affichera car bool(123) == True
    print("Il y a une valeur numérique (positive ou négative)")

if 0:
    # le message ne s'affichera pas car bool(0) == False
    print("Il y a une valeur nulle")
