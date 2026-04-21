import random
import numpy as np



dico_couleur = {"bleu":1, "rouge":2, "violet":3, "jaune":4, "vert":5}




def grille_initiale(n,m): #renvoie une grille de taille n*m  et n//3 cases bloquées
    grille = []
    for i in range(n):
        grille.append([])
        for j in range(m):
            grille[i].append([True,"blanc"])
    grille = np.array(grille)
            
    nb_bloquees = n//3
    L = []
    
    compteur = 0
    
    while compteur < nb_bloquees:  
        a = random.randint(0,n-1)
        b = random.randint(0,m-1)
        if (a,b) not in L:
            compteur += 1
            L.append((a,b))
            grille[a][b] = [False,"noir"]
            
    return grille



def poly_aleatoire(n_poly,m_poly,dico_couleur):  #longeur, largeur, couleur du poly
    
    poly = []
    couleur = None
    numero = random.randint(1,len(dico_couleur))
    for x in dico_couleur:
        if dico_couleur[x] == numero:
            couleur = x
    for i in range(n_poly):
        poly.append([])
        for j in range(m_poly):
           poly[i].append(couleur)
    return poly


print(poly_aleatoire(2,2,dico_couleur))
# print(grille_initiale(6,6))
    