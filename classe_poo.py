import TP_CARTO



class Case:
    def __init__(self, disponibilite, couleur):
        self.disponibilite = disponibilite
        self.couleur = couleur

class Polymino(Case) :
    def __init__(self, occupation, couleur, forme):
        self.forme = forme
        self.couleur = couleur
        
# class Case_bloque(self, disponibilite, couleur) : 
#     def __init__(self, )

class Grille :
    def __init__(self, tableau):
        self.tableau = tableau
        
        
    def integration(self,poly,case_depart):
        
        for i in range(len(self.tableau)):
            for j in range(len(self.tableau[i])):
                poly[]
        
        
        
    

# if __name__ == "__main__":
#     case1 = Case(True, "green")
    
    
    