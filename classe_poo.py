class Case:
    def __init__(self, disponibilite, couleur):
        self.disponibilite = disponibilite
        self.couleur = couleur
        

class Polymino(Case) :
    def __init__(self, occupation, couleur, forme):
        self.forme = forme
        self.couleur = couleur
        
class Case_bloque : 