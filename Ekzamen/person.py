class Death(BaseException):
    def __init__(self, message=""):
        BaseException.__init__(self, message)
        self.message = message

    def __str__(self):
        return self.message


class Depression(BaseException):
    def __init__(self, message=""):
        BaseException.__init__(self, message)
        self.message = message

    def __str__(self):
        return self.message


class Bankrot(BaseException):
    def __init__(self, message=""):
        BaseException.__init__(self, message)
        self.message = message

    def __str__(self):
        return self.message


class Person:
    name = ''
    health = 0
    mood = 0
    money = 0

    def __init__(self, name='', health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return \
            f'Имя: {self.name}\n' \
            f'Состояние здоровья: {self.health}\n' \
            f'Настроение: {self.mood}\n' \
            f'Капитал: {self.money}\n'

    def change_state(self, money, health, mood):
        if self.money <= 0:
            raise Bankrot(f'{self.name} обанкротился(ась)')
        else:
            self.money += money

        if self.health <= 0:
            raise Death(f'{self.name} скончался(ась)')
        else:
            self.health += health

        if self.mood <= 0:
            raise Depression(f'{self.name} впал(а) в депрессию')
        else:
            self.mood += mood

    def do(self, action):
        if self.money <= 0:
            raise Bankrot(f'{self.name} обанкротился(ась)')
        else:
            self.money += action.money

        if self.health <= 0:
            raise Death(f'{self.name} скончался(ась)')
        else:
            self.health += action.health

        if self.mood <= 0:
            raise Depression(f'{self.name} впал(а) в депрессию')
        else:
            self.mood += action.mood
