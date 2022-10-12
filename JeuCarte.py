# Fichier JeuCarte.py

from Carte import *  # importation de la classe Carte
from random import *  # librairie permettant d'utiliser des nombres aléatoires

liste_familles = ["Pique", "Coeur", "Carreau", "Trèfle"]
liste_valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "As"]

class JeuCarte:  # définition de la classe
    def __init__(self, modele):  # méthode 1 : constructeur
        if modele in ["32", "52"]:
            self.modele = modele  # création du premier attribut
            if modele == "32":
                self.jeu = [Carte(v, f) for v in liste_valeurs[5:] for f in liste_familles]  # création du deuxième attribut
            else:
                self.jeu = [Carte(v, f) for v in liste_valeurs for f in liste_familles]  # création du deuxième attribut
        else:
            print("Création non licite")
            return None

    def getModele(self):  # méthode 2 : un 1er accesseur
        return self.modele

    def getJeu(self):  # méthode 3 : un 2ème accesseur
        return [c.getAttributs() for c in self.jeu]

    def setModele(self, modele):  # méthode 4 : un mutateur
        if modele == self.modele:
            pass
        elif modele in ["32", "52"]:
            self.modele = modele
            if modele == "32":
                self.jeu = [Carte(v, f) for v in liste_valeurs[5:] for f in liste_familles]  # création du deuxième attribut
            else:
                self.jeu = [Carte(v, f) for v in liste_valeurs for f in liste_familles]  # création du deuxième attribut
            return True
        else:
            return False

    def tirerUneCarte(self):  # méthode 5 : pour tirer une carte au hasard
        return choice(self.jeu).getAttributs()

    def melangerJeu(self):  # méthode 6 : pour mélanger le jeu
        shuffle(self.jeu)
        
