class Character:
    name = ""
    hp = 100
    dmg = 1
    defen = 0

    def is_alive(self):
        return self.hp > 0

    # Конструктор
    def __init__(self, name="", hp=100, dmg=1, defen=0):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.defen = defen

    def __str__(self):
        return \
            f"Name: {self.name}\n" \
            f"Hp: {self.hp}\n" \
            f"Dmg: {self.dmg}\n" \
            f"Defen: {self.defen}\n"

    def take_dmg(self, dmg):
        self.hp -= max(dmg, 0)

    def atk(self, enemy):
        enemy.take_dmg(self.dmg)

    def set_name(self, new_name):
        self.name = new_name




