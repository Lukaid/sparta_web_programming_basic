from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

matrix_rating = db.movies.find_one({'title':'매트릭스'},{'_id':False})['rating']

matrix_rating_list = list(db.movies.find({'rating':matrix_rating} ,{'_id':False}))