# -*- coding: utf-8 -*-
import random 
import numpy as np
from classe_poo import *


dico_couleur = {"bleu":1, "rouge":2, "violet":3, "jaune":4, "vert":5}
dico_couleur_inv = {1:"bleu", 2:"rouge", 3:"violet", 4:"jaune", 5:"vert"}


def grille_initiale(n,m): #renvoie une grille de taille n*m  et n//3 cases bloquées
    grille = []
    for i in range(n):
        grille.append([])
        for j in range(m):
            grille[i].append([0,"blanc"])
    #grille = np.array(grille)
            
    nb_bloquees = n//2
    L = []
    
    compteur = 0
    
    while compteur < nb_bloquees:  
        a = random.randint(0,n-1)
        b = random.randint(0,m-1)
        if (a,b) not in L:
            compteur += 1
            L.append((a,b))
            grille[a][b] = [1,"noir"]
            
    return grille

def poly_aleatoire(taille_max):
    #Choix de la couleur
    c = dico_couleur_inv[random.randint(1,5)]
    
    figure = {(0,0)}
    
    while len(figure) < taille_max:
        # print(figure)
        x,y = random.choice(list(figure))
              
        dx,dy = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        figure.add((x + dx, y + dy))
              
    fig_norm = figure_origine(figure)
    fig_color = figure_couleur(fig_norm, c)
    return fig_color

def figure_origine(figure):
    
    min_x = min(x for x,y in figure)
    min_y = min(y for x,y in figure)
    figure = {(x - min_x, y - min_y) for x,y in figure}
    max_x = max(x for x,y in figure)
    max_y = max(y for x,y in figure)
    figure_finale = [[0] * (max_y + 1) for i in range(max_x + 1)]
    for x,y in figure:
        figure_finale[x][y] = 1
    return figure_finale

def figure_couleur(figure_normalisee, couleur):
    new_fig = []
    for ligne in figure_normalisee :
        new_ligne = []
        for i in range(len(ligne)) :
            if ligne[i] == 1 :
                new_ligne.append([ligne[i], couleur])
            else : 
                new_ligne.append([ligne[i], "blanc"])
        new_fig.append(new_ligne)
    return new_fig
            

def verif_local(self):
    for ligne in self.tableau:
        for case in ligne:
            if case[0] >= 2:
                return False
    return True



def col_full(grille,col):

    for ligne in grille:
        if ligne[col][0] == 0: # si une case de la colonne est libre
            return False
    return True # si toute la colonne est pleine

def ligne_full(grille, ligne):
    for case in grille[ligne]:
        if case[0] == 0:
            return False # si une case de la ligne est libre
    return True # si toute la ligne est pleine



    

if __name__ == "__main__":
    
    print()
    print("Grille")
    grille = Grille(grille_initiale(5,5))
    print(grille)
    grille.affiche_couleur()
    print(len(grille))
    
    print()
    print("Polyomino")
    fig = Polyomino(poly_aleatoire(5))
    print(fig)
    fig.affiche_couleur()
    
    print()
    print("Placement de la pièce")
    grille.poser_piece(fig, 0, 0)
    print(grille)
    
    for ligne in grille :
        print(ligne[0])
    print(grille.score_variantes())







    