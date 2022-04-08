class Enfant:

    def __init__(self, nom="", prenom="", id=-1, localisation=""):
        
        self.nom = nom
        self.prenom = prenom
        self.id = id
        self.localisation = localisation
        self.loc_precedentes = [localisation]
        self.parents = []

    def add_parent(self, parent):

        self.parents.append(parent)
        print("Un parent a ete ajoute")
    
    def add_parents(self, parents):

        for parent in parents:
            self.add_parent(parent)
    
    def remove_parent(self, parent):

        if parent in self.parents:
            self.parents.remove(parent)
            print("Le parent a ete supprime")
        else:
            print("Ce parent n'existe pas")

    def new_localisation(self, localisation):

        if len(self.loc_precedentes) >= 10:
            del self.loc_precedentes[0]
        self.loc_precedentes.append(localisation)
        self.localisation = localisation

    def print_infos(self):
        print("\nJe suis un enfant, mes infos sont:")
        print("nom: ", self.nom)
        print("prenom: ", self.prenom)
        print("id: ", self.id)
        print("localisation: ", self.localisation)
        print("loc_precedentes: ", self.loc_precedentes)
        print("parents: ", self.parents)