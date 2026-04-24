import TP_CARTO


class Grille :
    def __init__(self, tableau):
        self.tableau = tableau
    
    def __str__(self):
        txt = ""
        for ligne in self.tableau :
            for element in ligne :
                txt += str(element[0])
                txt += ' '
            txt += "\n"
        return txt

class Polyomino(Grille) :
    def __init__(self, tableau):
        super().__init__(tableau)
    
    def __str__(self):
        super().__str__(self.tableau)
        
        
        
class Case:
    def __init__(self, disponibilite, couleur):
        self.disponibilite = disponibilite
        self.couleur = couleur


        
class Case_bloque(Case) : 
    def __init__(disponibilite, couleur):
        super().__init__(disponibilite, couleur)

        
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

    
