import random
import numpy as np



dico_couleur = {"bleu":1, "rouge":2, "violet":3, "jaune":4, "vert":5}




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
    figure = {(0,0)}
    
    while len(figure) < taille_max:
        print(figure)
        x,y = random.choice(list(figure))
              
        dx,dy = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        figure.add((x + dx, y + dy))
              
    return figure_origine(figure)

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

def verif_local(grille):
    for ligne in grille:
        for case in ligne:
            if case <= 3:
                return False
    return True

def poser_piece(grille, piece, x, y, couleur):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == 1:
                gx = x + i
                gy = y + j
                if gx >= len(grille) or gy >= len(grille[0]): 
                    raise IndexError (f"Coordonnée en dehors de la grille")
                grille[gx][gy][0] += 2
                grille[gx][gy][1] = couleur
    return grille

if __name__ == "__main__":
    fig = poly_aleatoire(6)
    print("a")
    print(fig)
    print("a")
    a = grille_initiale(5,5)
    aa = poser_piece(a, fig, 5, 5, "rouge")
    print(aa)





# print(poly_aleatoire(2,2,dico_couleur))
# print(grille_initiale(6,6))
    