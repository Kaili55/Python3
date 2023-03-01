from Urok2.character import Character
import random


class Assasin(Character):
    def __init__(self, name="", hp=100, dmg=1, defen=0):
        Character.__init__(self, name, hp, dmg, defen)

    def roll(self, possibility):
        return random.randint(1, 100) <= possibility

    def atk(self, enemy):
        if self.roll(10):
            enemy.take_dmg(1000)
        else:
            enemy.take_dmg(self.dmg)