from Urok2.character import Character


class Vampyre(Character):
    def __init__(self, name="", hp=100, dmg=1, defen=0):
        Character.__init__(self, name, hp, dmg, defen)

    def atk(self, enemy):
        enemy.take_dmg(self.dmg)
        self.hp = self.hp + self.dmg / 100 * 10
