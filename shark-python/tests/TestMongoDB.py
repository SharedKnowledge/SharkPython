import unittest
import json
import jsonpickle
from pymongo import MongoClient

from Knowledge import Knowledge
from KnowledgeBase import KnowledgeBase
from PeerSemanticTag import Address, PeerSemanticTag
from PredicateSemanticTag import PredicateSemanticTag
from SemanticNet import SemanticNet
from SemanticTag import *
from Vocabulary import Vocabulary


class TestMongoDB(unittest.TestCase):


    #client = MongoClient('localhost', 27017)

    def test_CRUD(self):
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
        property_tag.id = 10


    def test_semantic_tag_CRUD(self):
        property_tag = SemanticTag("Property", "ssn:Poperty")
        property_tag_json = jsonpickle.encode(property_tag)
        client = MongoClient()
        db = client.local
        collection = db.semantic_tags
        #print(type(property_tag_json))
        collection.insert_one(property_tag.__dict__)
        print(property_tag.__dict__)
        i =10
        property_tag_json_returned = db.semantic_tags.find_one( {
            "name": property_tag.name
        })
        #print(property_tag_json_returned["name"])
        #testList = property_tag_json_returned["si"]
        #print(property_tag_json_returned.keys())

    def test_knowledge_CRUD(self):
        tag_id = 0
        property_tag = SemanticTag("Property", "ssn:Poperty")
        measurement_property_tag = SemanticTag("Measurement Property", "ssn:property/MeasurementProperty")
        relation_tag1 = PredicateSemanticTag("is a", "http://www.w3.org/ns/ssn/#is_a", property_tag, measurement_property_tag)
        semanticNet = SemanticNet()
        semanticNet.add_tag(property_tag, tag_id)
        tag_id += 1
        semanticNet.add_tag(measurement_property_tag, tag_id)
        tag_id += 1
        semanticNet.add_predicate(relation_tag1)
        accuracy_tag = SemanticTag("Accuracy", "ssn:property/MeasurementProperty/Accuracy")
        relation_tag2 = PredicateSemanticTag("is a", "http://www.w3.org/ns/ssn/#is_a", measurement_property_tag, accuracy_tag)
        semanticNet.add_tag(accuracy_tag, tag_id)
        semanticNet.add_predicate(relation_tag2)
        vocabulary = Vocabulary(semanticNet, None, None, None, None)
        knowledge = Knowledge(vocabulary, None, None)
        kb = KnowledgeBase(knowledge)
        client = MongoClient()
        db = client.local
        collection = db.knowledge_base
        kb_json = jsonpickle.encode(kb)
        print("\n" + kb_json + "\n")
        #collection.insert_one(semanticNet.__dict__)




















