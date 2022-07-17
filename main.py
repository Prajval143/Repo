import pymongo


client = pymongo.MongoClient("mongodb+srv://Prajval:Prajval1998@cluster0.vzcbx6t.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Prajval",
    "email" : "prajvalmohan143@gmail.com",
    "surname" : "Wachkavade"
}
d = {
    "name":"Prajval",
    "email" : "prajvalmohan143@gmail.com",
    "surname" : "Wachkavade"
}
d = {
    "name":"Prajval",
    "email" : "prajvalmohan143@gmail.com",
    "surname" : "Wachkavade"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)