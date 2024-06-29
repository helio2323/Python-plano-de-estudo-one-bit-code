from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

old_value = { "content": "Conteudo do post 1" }
new_value = { "$set": { "content": "Conteudo do post 1 alterado" } }

mycol.update_one(old_value, new_value)


for x in mycol.find():
    print(x)