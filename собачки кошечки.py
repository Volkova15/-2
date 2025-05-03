class Animal():
    def __init__ (self, kind, legs):
        self.kind = kind
        self.legs = legs
    def description(self ):
        if self.legs == 1: print(self.kind, 'має', self.legs, 'кінцівку')
        else: print(self.kind, 'має', self.legs, 'кінцівки')
a1 = Animal('слон', 4)
a2 = Animal('курка', 2)
a3 = Animal('устриця', 0)
a1.description()
a2.description()
a3.description()
