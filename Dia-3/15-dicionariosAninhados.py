import pprint

gamesDict = {
    "resident evil 4":{
        "yearLaunch": 2023,
        "classification": 9.8,
        "genre": ["açao", "aventura"]
    },
    "Mario odyssey":{
        "yearLaunch": 2023,
        "classification": 9.8,
        "genre": ["açao", "aventura"]
    },
    "donkey kong":{
        "yearLaunch": 2023,
        "classification": 9.8,
        "genre": ["açao", "aventura"]
    },
}

pp = pprint.PrettyPrinter(depth=4)

#pp.pprint(gamesDict)

#busca informacao dentro de dicionario aninhado

print(gamesDict["Mario odyssey"]["genre"])

#2 - Adiciona novos itens

gamesDict["Mario odyssey"]["players"] = 1

print(gamesDict["Mario odyssey"])

#3 - excluir um dicionario

del gamesDict["resident evil 4"]

pp.pprint(gamesDict)