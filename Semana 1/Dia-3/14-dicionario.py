gameFifa = {
    "name": "Fifa 23",
    "year": "2022",
    "price": 90.50,
    "Classification": 8.5,
    "genre": ["Ação", "Tiro", "RPG"],
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperar um elemento do dicionario

print(gameFifa["genre"])
print(gameFifa.get("classification"))

# 2 - Recupear ou buscar as chaves do dicionario

print(gameFifa.keys())

# 3 - Recuperar apenas os valores do dicionario

print(gameFifa.values())

# 4 - Recuperar itens com chave e valor

print(gameFifa.items())

# 5 - Adicionar itens ao dicionario

gameFifa["publisher"] = "Electronic Arts"
print(gameFifa)

# 6 - Atualizar itens no dicionario
gameFifa.update({"Classification": 9.0})
print(gameFifa)

# 7 - Remover iten no dicionario

gameFifa.pop("price")
print(gameFifa)