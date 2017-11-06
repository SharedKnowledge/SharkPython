import bson
import jsonpickle
from pymongo import MongoClient
import json
"""The MongoHelper is a Helper Class for the developer. All CRUD methods concerning 
the storage of Knowledge into a MongoDB Database are implemented here."""
class MongoHelper:

    @staticmethod
    def save_knowledge(knowledge):
        client = MongoClient()
        db = client.local
        collection = db.knowledge_base
        knowledge_json = jsonpickle.encode(knowledge)
        knowledge_bson = bson.son.SON(json.loads(knowledge_json))
        collection.insert_one(knowledge_bson)

    @staticmethod
    def find_knowledge(knowledge_part): #Knowledge Parts can be Semantic Nets or Tags
        client = MongoClient()
        db = client.local
        collection = db.knowledge_base
        knowledge_part_json = jsonpickle.encode(knowledge_part)
        knowledge_part_bson = bson.son.SON(json.loads(knowledge_part_json))
        return collection.find_one(knowledge_part_bson)

    @staticmethod
    def delete_knowledge(knowledge_part): #Knowledge Parts can be Semantic Nets or Tags
        client = MongoClient()
        db = client.local
        collection = db.knowledge_base
        knowledge_part_json = jsonpickle.encode(knowledge_part)
        knowledge_part_bson = bson.son.SON(json.loads(knowledge_part_json))
        collection.delete_one(knowledge_part_bson)

    @staticmethod
    def update_knowledge(knowledge_part): #Knowledge Parts can be Semantic Nets or Tags
        client = MongoClient()
        db = client.local
        collection = db.knowledge_base
        knowledge_part_json = jsonpickle.encode(knowledge_part)
        knowledge_part_bson = bson.son.SON(json.loads(knowledge_part_json))
        collection.update_one(knowledge_part_bson)

    @staticmethod
    def save_kb_object(object, collection_name):
        client = MongoClient()
        db = client.local
        collection = db[collection_name]
        object_json = jsonpickle.encode(object)
        object_json = bson.son.SON(json.loads(object_json))
        collection.insert_one(object_json)