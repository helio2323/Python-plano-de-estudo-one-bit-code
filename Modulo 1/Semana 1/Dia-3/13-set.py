gameSet = {"The Witcher 3", "Red Dead Redemption 2", "The Legend of Zelda: Breath of the Wild", "Cyberpunk 2077", "Super Mario Odyssey"}

print(gameSet)

# 1 - Buscar o tamanho do set
print(len(gameSet))

# 2 - True e 1 sao considerados o mesmo valor

examPleSet = {"Fifa 23", True, 1, 90.50}
print(examPleSet)

# 3 - Adicionar item de outro set

gameSet.update(examPleSet)
print(gameSet)

# 4 - Remover itens do gameSet

gameSet.remove(90.50)
gameSet.remove(True)

print(gameSet)

# - Nao possibilida recuperar valores via fatiamento ou slice

