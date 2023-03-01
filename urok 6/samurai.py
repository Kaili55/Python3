from Urok2.character import Character


class Samurai(Character):
    def __init__(self, name="", hp=100, dmg=1, defen=0):
        Character.__init__(self, name, hp, dmg, defen)

        self.start_dmg = self.dmg
        self.dmg_add = 0

    def atk(self, enemy):
        if self.dmg_add < 5:
            add = self.start_dmg / 100 * 10
            self.dmg += add
            self.dmg_add += 1
        else:
            self.dmg_add = 0
            self.dmg = self.start_dmg
        enemy.take_dmg(self.dmg)
