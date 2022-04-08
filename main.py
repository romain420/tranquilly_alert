from Parent import Parent
from Enfant import Enfant

enfant1 = Enfant("Roger", "Marg", 0, "maison")
enfant2 = Enfant("Adolph", "Marg", 1, "ecole")
enfant3 = Enfant("Pascal", "Lite", 2, "rue")
parent1 = Parent("Tic", "Marg", 3)
parent2 = Parent("Tac", "Marg", 4)

parent1.add_enfants([enfant1, enfant2])
parent2.add_enfants([enfant1, enfant2])

enfant1.print_infos()
enfant1.new_localisation("rue")
enfant1.print_infos()
enfant1.new_localisation("ecole")
enfant1.print_infos()
enfant1.new_localisation("rue")
enfant1.print_infos()
enfant1.new_localisation("maison")
enfant1.print_infos()
enfant1.new_localisation("grandparents")
enfant1.print_infos()