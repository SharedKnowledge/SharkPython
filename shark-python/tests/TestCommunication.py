from KnowledgeBase import *
from Knowledge import *
import unittest
import jsonpickle


class MyTest(unittest.TestCase):

    def testExpose(self):
        pass


    def testInsert(self):
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

        semanticNetJson = jsonpickle.encode(semanticNet)
        print(semanticNetJson)
        semanticNetDecoded = jsonpickle.decode(semanticNetJson)


        tag_id += 1
        resolution_tag = SemanticTag("Resolution", "ssn:Resolution")
        semanticNet2 = SemanticNet()
        semanticNet2.add_tag(resolution_tag, tag_id)
        tag_id += 1
        measurement_property_tag2 = SemanticTag("Measurement Property", "ssn:property/MeasurementProperty")
        semanticNet2.add_tag(measurement_property_tag2, tag_id)
        relation_tag3 = PredicateSemanticTag("is a", "http://www.w3.org/ns/ssn/#is_a", measurement_property_tag, resolution_tag)
        semanticNet2.add_predicate(relation_tag3)
        vocabulary2 = Vocabulary(semanticNet2, None, None, None, None)
        knowledge2 = Knowledge(vocabulary2, None, None)
        kb2 = KnowledgeBase(knowledge2)

        kb.insert(kb2.knowledge)


        i = 30






