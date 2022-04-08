from Parent import Parent
from Enfant import Enfant


enfant1 = Enfant("Roger", "Marg",  0, (0,0))
enfant2 = Enfant("Adolph", "Marg", 1, (1,0))
enfant3 = Enfant("Pascal", "Lite", 2, (0,1))
parent1 = Parent("Tic", "Marg", 3)
parent2 = Parent("Tac", "Marg", 4)

parent1.add_enfants([enfant1, enfant2])
parent2.add_enfants([enfant1, enfant2])

enfant1.print_infos()
enfant1.new_localisation((1,0))
enfant1.print_infos()

parent1.add_repere_to_enfant((100,100), enfant1)
enfant1.am_i_too_far()
enfant1.new_localisation((99,99))
enfant1.am_i_too_far()
