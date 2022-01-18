import pymongo

from pymongo import MongoClient

cluster = MongoClient('mongodb+s://shah476:Shahjee1977@cluster0.dq7wl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["test"]
collection=db["test"]

results=collection.find({})

for result in results:
    print (result)
    
print ("="*30)

results1=collection.find({"cities.population":151})
print(results1)

for el in results1:
    print(el)