class Animal():
    def __init__ (self, kind, legs):
        self.kind = kind
        self.legs = legs
    def description(self):
        if self.legs == 1: print(self.kind,'має', self.legs, 'кінцівку')
        else: print(self.kind,'має', self.legs, 'кінцівки')

class Cat(Animal):
    pass

class Dog(Animal):
    pass

a1 = Animal('павук', 8)
a2 = Cat('кіт Марс', 4)
a3 = Animal('риба', 0)
a4 = Dog('Джері', 4)
a1.description()
a2.description()
a3.description()
a4.description()