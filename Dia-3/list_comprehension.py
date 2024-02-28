# 1 - liste valores de 0 a 10 que sejam menor do que 4

listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

# 2 - jogos que tenham a letra a

gameList = ["Resident Evil 4", "Star Wars Jedi Survivor", "The Legend of Zelda", "Dark Souls 3", "Controle"]

newList = [game for game in gameList if "o" in game]

print(newList)

# 3 - Jogos que eu zerei

gamesFinished = [x for x in gameList if x != "Controle"]

print(gamesFinished)