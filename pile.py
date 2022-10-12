"""
Classe Pile
"""


class Pile:
    """
    Classe Pile implémentée avec un liste
    """

    def __init__(self, valeurs=None):
        """Initialisation de la pile"""
        self.valeurs = []
        if valeurs:
            if type(valeurs) == list:
                for val in valeurs:
                    self.valeurs.append(val)
            else:
                self.valeurs.append(valeurs)

    def pile_vide(self):
        """
        Vérifie si la pile est vide
        Renvoie un booléen
        """
        if len(self.valeurs) == 0:
            return True
        else:
            return False

    def push(self, element):
        """Ajoute un élément à la fin de la pile"""

        self.valeurs.append(element)

    def pop(self):
        """Supprime le dernier élément de la pile et le renvoie"""
        if not(self.pile_vide()):
            return self.valeurs.pop()
        else:
            return "List is empty"

    def sommet(self):
        """Renvoie le dernier élément de la pile"""
        if not(self.pile_vide()):
            return self.valeurs[-1]

    def taille(self):
        """Renvoie la taille de la pile"""
        return len(self.valeurs)

    def get_3_first_cards(self):
        main_de_base = []
        for e in range(3):
            main_de_base.append(self.pop())
        return main_de_base
    
    def get_all_cards(self):
        return self.valeurs
    
        
        

if __name__ == "__main__":
    pile1 = Pile([4, 3])
    pile1.push(1)
    pile2 = Pile()
    pile2.push(5)
    print(pile1.get_all_cards())
