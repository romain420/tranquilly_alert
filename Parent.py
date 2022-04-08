class Parent:

    def __init__(self, nom, prenom, id):

        self.nom = nom
        self.prenom = prenom
        self.id = id
        self.enfants = []

    def add_enfant(self, enfant):

        self.enfants.append(enfant)
        print("Un enfant a ete ajoute")
        enfant.add_parent(self)

    def add_enfants(self, enfants):

        for enfant in enfants:
            self.add_enfant(enfant)
    
    def remove_enfant(self, enfant):

        if enfant in self.enfants:
            self.enfants.remove(enfant)
            print("Le enfant a ete supprime")
        else:
            print("Ce parent n'existe pas")
        
    def print_infos(self):
        print("\nJe suis un parent, mes infos sont:")
        print("nom: ", self.nom)
        print("prenom: ", self.prenom)
        print("id: ", self.id)
        print("enfants: ", self.enfants)