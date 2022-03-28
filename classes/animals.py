class Animal:
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        return "Greetings, human."

class Cat(Animal):
    def greeting(self, maintain_illusion = False):
        if maintain_illusion == True:
            return "Nyan"
        return "Who are you? Have you got any food? Gimme your food or I'll hurt you."

class Chicken(Animal):
    def greeting(self, maintain_illusion = False):
        if maintain_illusion == True:
            return "Brraaaaaaawk!"
        return super().greeting() + " Please. Have mercy. Save me from my horrible, bloody fate."

seemingly_normal_chicken = Chicken("Harland")
disturbingly_intelligent_chicken = Chicken("David")

seemingly_normal_cat = Cat("Bagpuss")
disturbingly_intelligent_cat = Cat("Stephen")

print()
print(f"{seemingly_normal_chicken.name} the seemingly normal chicken: \"{seemingly_normal_chicken.greeting(True)}\"")
print(f"{disturbingly_intelligent_chicken.name} the disturbingly intelligent chicken: \"{disturbingly_intelligent_chicken.greeting()}\"")
print()
print(f"{seemingly_normal_cat.name} the seemingly normal cat: \"{seemingly_normal_cat.greeting(True)}\"")
print(f"{disturbingly_intelligent_cat.name} the disturbingly intelligent cat: \"{disturbingly_intelligent_cat.greeting()}\"")
print()
