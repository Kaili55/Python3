from Urok2.character import Character
import random


class Ninja(Character):
    def __init__(self, name="", hp=100, dmg=1, defen=0):
        Character.__init__(self, name, hp, dmg, defen)

    def roll(self, possibility):
        return random.randint(1, 100) <= possibility

    def take_dmg(self, dmg):
        if self.roll(15):
            self.hp = self.hp
        else:
            self.hp -= max(dmg, 0)
