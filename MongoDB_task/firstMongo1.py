import pymongo
import requests

from pymongo import MongoClient

cluster = MongoClient('mongodb+s://shah476:Shahjee1977@cluster0.dq7wl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["test"]
collection=db["test"]

results=[]

for i in range (9):
    url = "https://countries-cities.p.rapidapi.com/location/country/US/city/list"

    querystring = {"page":"2","per_page":"20","population":"1501"}

    headers = {
    'x-rapidapi-host': "countries-cities.p.rapidapi.com",
    'x-rapidapi-key': "962b4f2e6emshb65a974b3b3acd2p1673e4jsn430c5613d124"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    results.append(response.json())
    
collection.insert_many(results)