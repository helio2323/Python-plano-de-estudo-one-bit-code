gameList = ["Resident Evil 4", "Star Wars Jedi Survivor",
            "The Legend of Zelda", "Dark Souls 3"]


# 1 - Tamanho da lista

print(len(gameList))

# 2 - Recuperar um item da lista pelo indice

print(gameList.index("Star Wars Jedi Survivor"))

# 3 - Adicionar item ao final da lista

gameList.append("Dark Souls 4")
print(gameList)

# 4 - Ordernar a Lista

gameList.sort()

# 5 - Copiar itens de uma lista para outra

gameReset = gameList.copy()
gameReset.remove("Dark Souls 3")
print(gameReset)

# 6 - Remov todos os itens da lista

gameList.clear()
print(gameList)