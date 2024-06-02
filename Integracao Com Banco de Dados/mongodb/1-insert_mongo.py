from pymongo import MongoClient

client = MongoClient()
mydb = client.obcblog
mycol = mydb.posts

post1 = {
    'title': 'Post 1',
    'content': 'Conteudo do post 1',
    'author': {
        'name': 'Bruno',
        'email': 'pQpQs@example.com'
    }
}

result = mycol.insert_one(post1)
print(result.inserted_id)