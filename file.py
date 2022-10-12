"""
Classe File
"""


class File:
    def __init__(self, valeurs:list=[]):
        """Initialise la file"""
        self.valeurs = valeurs

    def file_vide(self):
        """
        Vérifie si la liste est vide
        Renvoie un booléen
        """
        if len(self.valeurs) == 0:
            return True
        else:
            return False

    def ajout(self, element):
        """Ajoute un élément au début de la file"""
        self.valeurs.insert(0, element)

    def retire(self):
        """Supprime et renvoie le dernier élément de la file"""
        return self.valeurs.pop()

    def premier(self):
        """Renvoie le dernier élément de la file"""
        return self.valeurs[-1]

    def taille(self):
        """Renvoie la taille de la file"""
        return len(self.valeurs)


if __name__ == "__main__":
    file = File([12, 14, 8, 7, 19, 22])