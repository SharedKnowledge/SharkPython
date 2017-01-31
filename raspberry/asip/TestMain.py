from PeerSemanticTag import  *
from PredicateSemanticTag import *
import unittest

class MyTest(unittest.TestCase):
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