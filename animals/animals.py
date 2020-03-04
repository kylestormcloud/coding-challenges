# Kyle Cloud
# Coding Challenges
# Date: March 4, 2020

from abc import ABC, abstractmethod

class Animal(ABC):    

    @abstractmethod
    def convert_to(self, animal):
        pass

# Parrot class extends Animal class
class Parrot(Animal):
    length = 1 # length in parrots
    type = "parrot"  

    @classmethod
    def convert_to(cls, animal):

        ratio = cls.length / animal.length

        print("One parrot is the same length as %s %ss." % (ratio, animal.type))

# Monkey class extends Animal class
class Monkey(Animal):
    length = 7.6 # length in parrots
    type = "monkey"

    @classmethod
    def convert_to(cls, animal):
        
        ratio = cls.length / animal.length

        print("One monkey is the same length as %s %ss." % (ratio, animal.type))

# Boa class extends Animal class
class Boa(Animal):
    length = 38 # length in parrots
    type = "boa"

    @classmethod
    def convert_to(cls, animal):

        ratio = cls.length / animal.length

        print("One boa is the same length as %s %ss." % (ratio, animal.type))
