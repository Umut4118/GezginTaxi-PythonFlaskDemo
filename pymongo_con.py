import pymongo
from pymongo import MongoClient
import pprint
import re


pp = pprint.PrettyPrinter(indent=4)
try:
    cluster = MongoClient("mongodb+srv://admin:admin@taxicenter.alsep.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster['Taxis']
    collection = db['Car1']
    print("bağlantı kuruldu")
except Exception as e:
    print(e)
a = collection.find({})
for element in a:
    Car1=element
Car1list=list(Car1.values())
Car1str = ''.join(map(str,Car1list))
Car1str=re.split('\n|,| ',Car1str)
Car1str[0]="2018-10-02"
print(Car1str[0])

try:
    cluster = MongoClient("mongodb+srv://admin:admin@taxicenter.alsep.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster['Taxis']
    collection = db['Car2']
except Exception as e:
    print(e)
a = collection.find({})
for element in a:
    Car2=element
Car2list=list(Car2.values())
Car2str = ''.join(map(str,Car2list))
Car2str=re.split('\n|,| ',Car2str)
Car2str[0]="2018-10-02"
print(Car2str[1])
try:
    cluster = MongoClient("mongodb+srv://admin:admin@taxicenter.alsep.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster['Taxis']
    collection = db['Car3']
except Exception as e:
    print(e)
a = collection.find({})
for element in a:
    Car3=element
Car3list=list(Car3.values())
Car3str = ''.join(map(str,Car3list))
Car3str=re.split('\n|,| ',Car3str)
Car3str[0]="2018-10-02"
print(Car3str[2])
try:
    cluster = MongoClient("mongodb+srv://admin:admin@taxicenter.alsep.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster['Taxis']
    collection = db['Car4']
except Exception as e:
    print(e)
a = collection.find({})
for element in a:
    Car4=element
Car4list=list(Car4.values())
Car4str = ''.join(map(str,Car4list))
Car4str=re.split('\n|,| ',Car4str)
Car4str[0]="2018-10-02"
print(Car4str[3])




