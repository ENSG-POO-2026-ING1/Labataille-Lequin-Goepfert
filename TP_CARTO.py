# -*- coding: utf-8 -*-
import random 
import numpy as np
import classe_poo


dico_couleur = {"bleu":1, "rouge":2, "violet":3, "jaune":4, "vert":5}
dico_couleur_inv = {1:"bleu", 2:"rouge", 3:"violet", 4:"jaune", 5:"vert"}

def affiche_disponibilite(grille) :
    for ligne in grille :
        for element in ligne :
            print(element[0], end=' ')
        print()

def affiche_couleur(grille) :
    for ligne in grille :
        for element in ligne :
            print(element[1], end=' ')
        print()


def grille_initiale(n,m): #renvoie une grille de taille n*m  et n//3 cases bloquées
    grille = []
    for i in range(n):
        grille.append([])
        for j in range(m):
            grille[i].append([0,"blanc"])
    #grille = np.array(grille)
            
    nb_bloquees = n//3
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
    print(c)
    
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
            

def verif_local(grille):
    for ligne in grille:
        for case in ligne:
            if case[0] >= 2:
                return False
    return True

def poser_piece(grille, piece, x, y):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j][0] == 1:
                gx = x + i
                gy = y + j
                
                if gx >= len(grille) or gy >= len(grille[0]) or gx < 0 or gy < 0: 
                    raise IndexError (f"Coordonnée en dehors de la grille")
                else :
                    grille[gx][gy][0] = piece[i][j][0] #disponibilite
                    grille[gx][gy][1] = piece[i][j][1]#couleur

    return grille


    

if __name__ == "__main__":


    grille = grille_initiale(5,5)
    affiche_disponibilite(grille)
    fig = poly_aleatoire(5)
    print(fig)
    # affiche_couleur(fig)
    affiche_disponibilite(fig)
    print()
    grille1 = poser_piece(grille, fig, 0, 0)
    affiche_disponibilite(grille1)
    affiche_couleur(grille1)
    # jouer()







    