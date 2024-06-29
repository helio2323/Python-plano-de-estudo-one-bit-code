import requests
from pymongo import MongoClient

client = MongoClient()

db = client['nobel']

response = requests.get("https://api.nobelprize.org/v1/prize.json")

for collection_name in ["prizes", "laureates"]:
    response = requests.get(f"https://api.nobelprize.org/v1/{collection_name[:-1]}.json")
    
    documents = response.json()[collection_name]

    print(f"Importando {collection_name}...")
    
    db[collection_name].insert_many(documents)

#Acesando colecoes

prizes = db['prizes'].find()
laureates = db['laureates'].find()

len_prizes = 0
len_laureates = 0

for prize in prizes:
    len_prizes += 1

for laureate in laureates:
    len_laureates += 1

print(f"prizes: {len_prizes}")
print(f"laureates: {len_laureates}")