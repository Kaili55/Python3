from Urok2.character import Character


class Berserc(Character):
    def __init__(self, name="", hp=100, dmg=1, defen=0):
        Character.__init__(self, name, hp, dmg, defen)

        self.add_dmg = 0
        self.max_hp = hp

    def take_dmg(self, dmg):
        super(Berserc, self).take_dmg(dmg=dmg)

    def atk(self, enemy):
        self.add_dmg= \
            max(
                (1 - self.hp / self.max_hp) * self.dmg,
                0
            )
        enemy.take_dmg(self.dmg + self.add_dmg)