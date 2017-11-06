from PeerSemanticTag import  *
from SemanticNet import *
import unittest

class MyTest(unittest.TestCase):

    address_max = None
    address_maxima = None
    peer_tag_max = None
    peer_tag_maxima = None
    predicate_tag = None

    def test_tags(self):
        address_max = Address("mail://s0123456@htw-berlin.de")
        address_maxima = Address("mail://s0123457@htw-berlin.de")
        peer_tag_max = PeerSemanticTag("Max Mustermann", "https://studi.f4.htw-berlin.de/~s0123456/", address_max)
        peer_tag_maxima = PeerSemanticTag("Maxima Mustermann", "https://studi.f4.htw-berlin.de/~s0123457/", address_maxima)
        predicate_tag = PredicateSemanticTag("Marriage", "https://en.wikipedia.org/wiki/Marriage", peer_tag_max.si, peer_tag_maxima.si)
        assert address_max is not None
        assert address_maxima is not None
        assert peer_tag_max is not None
        assert peer_tag_maxima is not None
        assert predicate_tag is not None
        assert address_max.email is True
        assert address_maxima.email is True
        assert "mail://s0123456@htw-berlin.de" in address_max.endpoint
        assert "mail://s0123457@htw-berlin.de" in address_maxima.endpoint
        assert peer_tag_max.address == address_max
        assert peer_tag_maxima.address == address_maxima
        assert "https://en.wikipedia.org/wiki/Marriage" in predicate_tag.si
        assert predicate_tag.source_si == peer_tag_max.si
        assert  predicate_tag.target_si == peer_tag_maxima.si

    def test_semantic_net(self):
        tag_id = 0
        semantic_net = SemanticNet()
        tag_example = SemanticTag("Test", "www.example.org")
        semantic_net.add_tag(tag_example, tag_id)
        ++tag_id
        assert semantic_net.st_table[tag_id] == tag_example
        assert "www.example.org" in semantic_net.st_table[tag_id].si

        tag_example2 = SemanticTag("Test2", "www.example.org/2")
        predicate_example = PredicateSemanticTag("ExamplePredicate", "https://en.wikipedia.org/wiki/Relation", tag_example.si, tag_example2.si)
        semantic_net.add_predicate(predicate_example)
        assert predicate_example in semantic_net.predicates



