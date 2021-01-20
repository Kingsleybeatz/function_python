from random import *
pierre = 1
feuille = 2
ciseaux = 3
n = 0
b = 0
while n<4 and b<4:
    joueur = int(input("choisissez pierre = 1, feuille = 2 ou ciseaux = 3 "))
    if joueur == 1:
        result_joueur = "pierre"
    elif joueur == 2:
        result_joueur = "feuille"
    elif joueur == 3:
        result_joueur = "ciseaux"

    a = randint(1,3)
    if a == 1:
        result = "pierre"
    elif a == 2:
        result = "feuille"
    elif a == 3:
        result = "ciseaux"

    if a == joueur:
        print("égalité")
    if a == 1 and joueur == 2:
        print("le joueur a gagné")
        n+=1
    if a == 1 and joueur == 3:
        print("L'ordinateur a gagné")
        b+=1
    if a == 2 and joueur == 1:
        print("L'ordinateur a gagné")
        b+=1
    if a == 2 and joueur == 3:
        print("Le joueur a gagné")
        n+=1
    if a == 3 and joueur == 1:
        print("le joueur a gagné")
        n+=1
    if a == 3 and joueur == 2:
        print("L'ordinateur a gagné")
        b+=1
    print(result_joueur,result )
    print("vous avez " , n, "point")
    print(" ordi a " , b,"point" )

