from Vocabulary import *
import unittest

class MyTest(unittest.TestCase):

    def test_property(self):
        tag_id = 0
        property_tag = SemanticTag("Property", "ssn:Poperty")
        measurement_property_tag = SemanticTag("Measurement Property", "ssn:property/MeasurementProperty")
        relation_tag1 = PredicateSemanticTag("is a", "http://www.w3.org/ns/ssn/#is_a", property_tag, measurement_property_tag)
        #Relationstag evtl. nicht nötig, da "is a" durch URI Hierarchie dargestellt werden kann
        semanticNet = SemanticNet()
        semanticNet.add_Tag(property_tag, tag_id)
        tag_id += 1
        semanticNet.add_Tag(measurement_property_tag, tag_id)
        tag_id += 1
        semanticNet.add_predicate(relation_tag1)
        accuracy_tag = SemanticTag("Accuracy", "ssn:property/MeasurementProperty/Accuracy")
        relation_tag2 = PredicateSemanticTag("is a", "http://www.w3.org/ns/ssn/#is_a", measurement_property_tag, accuracy_tag)
        semanticNet.add_Tag(accuracy_tag, tag_id)
        semanticNet.add_predicate(relation_tag2)

        vocabulary = Vocabulary(semanticNet, None, None, None, None)

        assert vocabulary.topic_dim.st_table[0] == property_tag
        assert vocabulary.topic_dim.st_table[1] == measurement_property_tag
        assert vocabulary.topic_dim.st_table[2] == accuracy_tag
        assert relation_tag1 in vocabulary.topic_dim.predicates
        assert relation_tag2 in vocabulary.topic_dim.predicates









