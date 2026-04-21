

class Case:
    def __init__(self, disponibilite, couleur):
        self.disponibilite = disponibilite
        self.couleur = couleur

class Polyomino(Case) :
    def __init__(self, occupation, couleur, forme):
        self.forme = forme
        self.couleur = couleur
        
        
class Case_bloque(Case) : 
    def __init__(disponibilite, couleur):
        super().__init__(disponibilite, couleur)
    
        

class Grille :
    def __init__(self, tableau):
        self.tableau = tableau
        
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
        pass
        
        
if __name__ == "__main__":
    case1 = Case(True, "green")
    
    
    