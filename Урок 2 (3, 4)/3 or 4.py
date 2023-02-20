from character import Character

player1 = Character(name="Margo", dmg=3, defen=1)
player2 = Character(name="Anatoliy", dmg=1, defen=1, hp=120)

print(f" - Player 1 - \n{player1}")
print(f" - Player 2 - \n{player2}")

player1.atk(player2)
print("Player 1 attaked Player 2")
player2.atk(player1)
print("Player 2 attaked Player 1")

print(f" - Player 1 - \n{player1}")
print(f" - Player 2 - \n{player2}")
