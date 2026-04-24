import TP_CARTO
import numpy as np
import random

dico_couleur = {"bleu":1, "rouge":2, "violet":3, "jaune":4, "vert":5}
dico_couleur_inv = {1:"bleu", 2:"rouge", 3:"violet", 4:"jaune", 5:"vert"}

class Grille :

    ### Constructeur
    def __init__(self, tableau):
        self.tableau = tableau
    
    ### Surcharge
    def __str__(self):
        txt = ""
        for ligne in self.tableau :
            for element in ligne :
                txt += str(element[0])
                txt += ' '
            txt += "\n"
        return txt
    
    def __len__(self):
        return len(self.tableau)
    
    ### Methodes
    def affiche_couleur(self) :
        for ligne in self.tableau :
            for element in ligne :
                print(element[1], end=' ')
            print()
    
    def poser_piece(self, piece, x, y): # Propre aux grilles mais pas aux poly ? 
        for i in range(len(piece)):
            for j in range(len(piece.tableau[0])):
                if piece.tableau[i][j][0] == 1:
                    gx = x + i
                    gy = y + j
                    
                    if gx >= len(self.tableau) or gy >= len(self.tableau[0]) or gx < 0 or gy < 0: 
                        raise IndexError (f"Coordonnée en dehors de la grille")
                    else :
                        self.tableau[gx][gy][0] = piece.tableau[i][j][0] #disponibilite
                        self.tableau[gx][gy][1] = piece.tableau[i][j][1] #couleur

class Polyomino(Grille) :
    def __init__(self, tableau):
        super().__init__(tableau)
        
    
        
# class Case:
#     def __init__(self, disponibilite, couleur):
#         self.disponibilite = disponibilite
#         self.couleur = couleur


        
# class Case_bloque(Case) : 
#     def __init__(disponibilite, couleur):
#         super().__init__(disponibilite, couleur)

        
class Partie :
    def __init__(self, id_partie, tour, largeur_grille, longueur_grille, nombre_case_bloquee):
        self.id_partie = id_partie
        self.tour = tour
        self.largeur_grille = largeur_grille
        self.longueur_grille = longueur_grille
        self.nombre_case_bloquee = nombre_case_bloquee
    
    # Methodes
    def jouer(param):
        pass


class Figure():
    def __init__(self, nom, description, nombre_de_point, etat):
        self.nom = nom                              # 'O', 'I', 'T' par ex
        self.descritpion = descritpion              # toute une colonne/ligne remplie
        self.nombre_de_point = nombre_de_point      # Nombre de points si cette figure est réalisée. 
        self.score = 0                              # Initialisation du score
    
    # Methodes
    def est_respectee(): #nico est dessus
        def col_full(grille,col):

            for ligne in grille:
                if ligne[col][0] == '0': # si une case de la colonne est libre
                    return False
            return True # si toute la colonne est pleine

        def ligne_full(grille, ligne):
            for case in grille[ligne]:
                if case[0] == '0':
                    return False # si une case de la ligne est libre
            return True # si toute la ligne est pleine
        
        
        
if __name__ == "__main__":
    case1 = Case(True, "green")

    
