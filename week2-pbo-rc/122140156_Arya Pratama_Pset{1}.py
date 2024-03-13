import random

class father :
    def __init__ (self, blood):
        self.type = blood

class mother :
    def __init__ (self):
        self.type = blood

class child :
    def __init__ (self):
        super().__init__(self.determine_child_blood_type(father, mother))

    def determine_allele_type(self, father, mother):
        alel_dad = random.choice(father[0:2 if len(father) > 2 else 1])
        alel_mom = random.choice(mother[0:2 if len(mother) > 2 else 1]) 
        factor = random.choice([father[-1], mother[-1]])  
        return [alel_dad, alel_mom, factor]
    
    def blood_child(self, alel) :
        if alel == 'AA':
            return 'A'
        elif alel == 'OA':
            return 'A'
        elif alel == 'BB':
            return 'B'
        elif alel == 'OB':
            return 'B'
        elif alel == 'AB':
            return 'AB'
        elif alel == 'OO':
            return 'O'

father_type = input("Father type blood : ")
mother_type = input("Mother type blood : ")

dad = father(father.type)
mom = mother(mother.type)
child(dad, mom)