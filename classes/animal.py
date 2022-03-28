class Animal:
    def disturbingly_intelligent_greeting(self):
        return "Greetings, human."

class Cat(Animal):
    def disturbingly_intelligent_greeting(self, maintain_illusion = False):
        if maintain_illusion == True:
            return "Nyan"
        return "Who are you? Have you got any food? Gimme your food."

class Chicken(Animal):
    def disturbingly_intelligent_greeting(self, maintain_illusion = False):
        if maintain_illusion == True:
            return "Brraaaaaaawk!"
        return super().disturbingly_intelligent_greeting()
