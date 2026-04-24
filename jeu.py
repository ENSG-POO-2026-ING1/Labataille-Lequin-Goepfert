from TP_CARTO import * 
import random


def jouer():
    
    n = input("Vous souhaitez jouer dans quel mode de diffilculté ? Facile/Moyen/Difficil ")
    if n == "F" or n == "f":
        t = 5
        grille = grille_initiale(t,t)
    elif n == "M" or n == "m":
        t = 7
        grille = grille_initiale(t,t)
    elif n == "D" or n =="d":
        t = 11
        grille = grille_initiale(t,t)
    else : 
        raise KeyError (f"Vous devez choisir un mode de difficulté")
    tour = 0
    while verif_local(grille):
        taille = random.randint(1,t)
        fig = poly_aleatoire(taille)
        print("Voici ta grille :")
        print()
        affiche_disponibilite(grille)
        print()
        print("Voici ta grille de couleur:")
        print()
        affiche_couleur(grille)
        print()

        
        print("Voici ton polyomino :")
        print()
        affiche_disponibilite(fig)
        x = int(input("Donne la colonne où tu veux que ta case du haut à gauche se place : " ))
        y = int(input("Donne la ligne où tu veux que ta case du haut à gauche se place : " ))
        poser_piece(grille, fig, x, y)
        tour += 1
    print("Voici ta grille :")
    print()
    affiche_disponibilite(grille)
    print()
    print("Voici ta grille de couleur:")
    print()
    affiche_couleur(grille)
    resultat = score(grille)
    print(resultat)
    
def score(grille):
    score = 0
    for ligne in range(len(grille)):
        if col_full(grille, ligne) :
            score += 2
    
    for col in range(len(grille[0])):
        if ligne_full(grille, col):
            score += 2
    score_couleur = score_variantes(grille)
    score_final = score + score_couleur

    return score_final

if __name__ == "__main__":
    jouer()
    # grille  = [[[1, 'blanc'], [1, 'blanc'], [1, 'blanc'], [1, 'blanc'], [1, 'blanc']],
    #  [[1, 'blanc'], [1, 'jaune'], [1, 'blanc'], [1, 'violet'], [1, 'jaune']],
    #  [[1, 'jaune'], [1, 'gris'], [1, 'blanc'], [1, 'blanc'], [1, 'blanc']],
    #  [[1, 'blanc'], [1, 'jaune'], [1, 'noir'], [1, 'bleu'], [1, 'rouge']],
    #  [[1, 'blanc'], [1, 'blanc'], [1, 'blanc'], [1, 'blanc'], [1, 'blanc']]]
    # s = score_variantes(grille)
    # a = score(grille)
    # r = a + s
    # print(r)