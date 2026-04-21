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
        
    

if __name__ == "__main__":
    case1 = Case(True, "green")
    
    
    