import random
from person import Person
from person import Bankrot
from person import Depression
from person import Death
from action import Action
from work import Work
from rest import Rest


work = Work(name="Сходить на работу:",
            money=random.randint(50, 100),
            mood=random.randint(-20, -10),
            health=random.randint(-10, -5))

rest = Rest(name="Отдохнуть:",
            money=random.randint(-10, -1),
            mood=random.randint(5, 7),
            health=random.randint(3, 5))

hospital = Action(name="Сходить в больницу:",
                  money=random.randint(-80, -50),
                  mood=random.randint(-5, 5),
                  health=random.randint(15, 25))

count = 0
human1 = Person(name='Толик', health=100, mood=100, money=5)
print(human1)
human2 = Person(name='Софа', health=100, mood=90, money=15)
print(human2)
human3 = Person(name='Мухамед', health=110, mood=120, money=50)
print(human3)
list1 = {rest, work, hospital}

while True:
    if human1 is not None:
        try:
            counter = random.randint(1, 3)
            if counter == 1:
                print(rest.name)
                if human1.health < 40:
                    rest.mood -= rest.mood * 0.2
                    human1.do(rest)
                else:
                    human1.do(rest)
                print(human1)
            elif counter == 2:
                print(work.name)
                if human1.mood > 90:
                    work.money += work.money * 0.1
                    human1.do(work)
                else:
                    human1.do(work)
                print(human1)
            else:
                print(hospital.name)
                human1.do(hospital)
                print(human1)
        except Death:
            print(Death, f'{human1.name} скончался(ась)')
            count += 1
            human1 = None
        except Depression:
            print(Depression, f'{human1.name} впал(а) в депрессию')
            count += 1
            human1 = None
        except Bankrot:
            print(Bankrot, f'{human1.name} обанкротился(ась)')
            count += 1
            human1 = None
        except Exception as error:
            print(error)

    if human2 is not None:
        try:
            counter = random.randint(1, 3)
            if counter == 1:
                print(rest.name)
                if human2.health < 40:
                    rest.mood -= rest.mood * 0.2
                    human2.do(rest)
                else:
                    human2.do(rest)
                print(human2)
            elif counter == 2:
                print(work.name)
                if human2.mood > 90:
                    work.money += work.money * 0.1
                    human2.do(work)
                else:
                    human2.do(work)
                print(human2)
            else:
                print(hospital.name)
                human2.do(hospital)
                print(human2)
        except Death:
            print(Death, f'{human2.name} скончался(ась)')
            count += 1
            human2 = None
        except Depression:
            print(Depression, f'{human2.name} впал(а) в депрессию')
            count += 1
            human2 = None
        except Bankrot:
            print(Bankrot, f'{human2.name} обанкротился(ась)')
            count += 1
            human2 = None
        except Exception as error:
            print(error)

    if human3 is not None:
        try:
            counter = random.randint(1, 3)
            if counter == 1:
                print(rest.name)
                if human3.health < 40:
                    rest.mood -= rest.mood * 0.2
                    human3.do(rest)
                else:
                    human3.do(rest)
                print(human3)
            elif counter == 2:
                print(work.name)
                if human3.mood > 90:
                    work.money += work.money * 0.1
                    human3.do(work)
                else:
                    human3.do(work)
                print(human3)
            else:
                print(hospital.name)
                human3.do(hospital)
                print(human3)
        except Death:
            print(Death, f'{human3.name} скончался(ась)')
            count += 1
            human3 = None
        except Depression:
            print(Depression, f'{human3.name} впал(а) в депрессию')
            count += 1
            human3 = None
        except Bankrot:
            print(Bankrot, f'{human3.name} обанкротился(ась)')
            count += 1
            human3 = None
        except Exception as error:
            print(error)

    if count == 3:
        break

