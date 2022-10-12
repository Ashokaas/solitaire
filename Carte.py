class Carte:  # définition de la classe
    def __init__(self, val, fam):  # méthode 1 : constructeur
        self.valeur = val  # création du premier attribut
        self.famille = fam  # création du deuxième attribut

    def getAttributs(self):  # méthode 2 : un 1er accesseur
        return [self.valeur, self.famille, "shown"]

    def getValeur(self):  # méthode 3 : un 2ème accesseur
        return self.valeur

    def getFamille(self):  # méthode 4 : un 3ème accesseur
        return self.famille

    def setValeur(self, val):  # méthode 5 : un 1er mutateur
        if val in ["7", "8", "9", "10", "V", "D", "R", "As"]:
            self.valeur = val
            return True
        else:
            return False

    def setFamille(self, fam):  # méthode 6 : un 2ème mutateur
        if fam in ["Pique", "Coeur", "Carreau", "Trèfle"]:
            self.famille = fam
            return True
        else:
            return False
