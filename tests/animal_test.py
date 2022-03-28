import unittest

from classes.animal import *

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal = Animal()
        self.cat = Cat()
        self.chicken = Chicken()
    
    def test_animal_is_disturbing(self):
        self.assertEqual("Greetings, human.", self.animal.disturbingly_intelligent_greeting())
    
    def test_cat_is_disinterested(self):
        self.assertEqual("Who are you? Have you got any food? Gimme your food.", self.cat.disturbingly_intelligent_greeting())
    
    def test_cat_is_elusive(self):
        self.assertEqual("Nyan", self.cat.disturbingly_intelligent_greeting(True))
    
    def test_chicken_can_talk(self):
        self.assertEqual("Greetings, human.", self.chicken.disturbingly_intelligent_greeting())

    def test_chicken_is_elusive(self):
        self.assertEqual("Brraaaaaaawk!", self.chicken.disturbingly_intelligent_greeting(True))