from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert / find / update / delete

doc = {'name':'bobby','age':21}
doc = {'name':'john','age':27}
doc = {'name':'smith','age':30}
doc = {'name':'jane','age':21}
db.users.insert_one(doc)

same_ages = list(db.users.find({'age':21},{'_id':False}))

# db.users.find({조건},{'_id':False}) # false는 가져오지 말라는 뜻, {조건}을 {}로 두면 all

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

db.users.delete_one({'name':'bobby'})