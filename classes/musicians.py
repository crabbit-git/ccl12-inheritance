class Musician:
    def __init__(self, name):
        self.name = name
        self.skills = []
    
    def learn_instrument(self, instrument):
        if instrument not in self.skills:
            self.skills.append(instrument)
    
    def skillset(self):
        if len(self.skills) == 2:
            return f"{self.name} can perform {self.skills[0]} and {self.skills[1]}."
        elif len(self.skills) >2:
            return f"{self.name} is a multi-instrumentalist."
        return f"{self.name} can perform {self.skills[0]}."

class Singer(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.skills = ["vocals"]

class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.skills = ["guitar"]

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.skills = ["drums"]

steve = Singer("Steve")
gab = Guitarist("Gabriela")
phil = Drummer("Phil")

phil.learn_instrument("vocals")

print(steve.skillset())
print(gab.skillset())
print(phil.skillset())
