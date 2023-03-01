from Urok2.character import Character
from assasin import Assasin
from berserc import Berserc
from ninja import Ninja
from vampyre import Vampyre
from samurai import Samurai

player1 = Assasin(name="Margo", dmg=10, defen=1)
player2 = Samurai(name="Anatoliy", dmg=10, defen=1)

while player1.is_alive() and player2.is_alive():
    player1.atk(player2)
    print("Player 1 attaked Player 2")
    player2.atk(player1)
    print("Player 2 attaked Player 1")
    print(f" - Player 1 - \n{player1}")
    print(f" - Player 2 - \n{player2}")


if player1.is_alive():
    print("Player 1 has won!")
else:
    print("Player 2 has won!")