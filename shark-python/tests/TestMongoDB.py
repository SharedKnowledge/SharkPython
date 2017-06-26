import unittest
import json
from pymongo import MongoClient

from PeerSemanticTag import Address, PeerSemanticTag
from SemanticTag import *


class TestMongoDB(unittest.TestCase):


    #client = MongoClient('localhost', 27017)

    def test_semantic_tag_CRUD(self):
        client = MongoClient()
        db = client.local
        property_tag = SemanticTag("Property", "ssn:Poperty")
        #property_tag_json = json.dumps({'name':property_tag.name,
           #                             'id':property_tag.id, 'si':property_tag.si})
        collection = db.semantic_tags
        #a = type(property_tag_json)
        #property_tag_id = collection.insert_one(json.dumps({'name':property_tag.name})).inserted_id
        collection.insert_one(        {
            "id": str(property_tag.id),
            "name": property_tag.name,

        })
        collection.insert_one(        {
            "id": 10,
            "name": "example",

        })
        all = db.semantic_tags.find()
        cursor = db.semantic_tags.find_one( {
            "name": property_tag.name
        })

        db.semantic_tags.delete_one({"name": property_tag.name})
        after_delete = db.semantic_tags.find()

        db.semantic_tags.update_one({"name": "example"}, { "$set": {"name": "example_after_update"}})

        after_update = db.semantic_tags.find_one({"name": "example_after_update"})



        i = 19
















