from Knowledge import Knowledge
from KnowledgeBase import KnowledgeBase
from Vocabulary import *
import unittest

class MyTest(unittest.TestCase):

    def test_property(self):
        tag_id = 0
        property_tag = SemanticTag("Property", "ssn:Property")
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
        knowledge= Knowledge()
        knowledge.vocabulary = vocabulary
        kb = KnowledgeBase(knowledge)

        assert vocabulary.topic_dim.st_table[0] == property_tag
        assert vocabulary.topic_dim.st_table[1] == measurement_property_tag
        assert vocabulary.topic_dim.st_table[2] == accuracy_tag
        assert relation_tag1 in vocabulary.topic_dim.predicates
        assert relation_tag2 in vocabulary.topic_dim.predicates

        selectivity_tag = SemanticTag("Selectivity", "ssn:property/MeasurementProperty/Selectivity")
        resolution_tag = SemanticTag("Resolution", "ssn:property/MeasurementProperty/Resolution")

        semantic_net_insert = SemanticNet()
        semantic_net_insert.add_tag(selectivity_tag, 0)
        semantic_net_insert.add_tag(resolution_tag, 1)
        semantic_net_insert.add_tag(measurement_property_tag, 2)
        vocabulary_insert = Vocabulary(semantic_net_insert, None, None, None, None)
        knowledge_insert = Knowledge()
        knowledge_insert.vocabulary = vocabulary_insert
        #kb.insert(knowledge_insert, 0)

        kb.insert(knowledge_insert, 1)

        #kb.insert(knowledge_insert, 2)

        #kb.insert(knowledge_insert, 3)
















