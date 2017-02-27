from PredicateSemanticTag import *
from PeerSemanticTag import *

class PeerSemanticNet:
    pst_table = None
    predicates = None
    def __init__(self, pst_table = None, predicates = None):
        if (pst_table is None):
            self.pst_table = {}
        else:
            self.pst_table = pst_table
        if (predicates is None):
            self.predicates = []
        else:
            self.predicates = predicates

    def add_Tag(self, peer_semantic_tag, semantic_tag_id):
        if (isinstance(peer_semantic_tag, PeerSemanticTag)):
            self.pst_table[semantic_tag_id] = peer_semantic_tag
        else:
            raise ValueError("The argument must be an instance of PeerSemanticTag!")

    def add_predicate(self, predicate_tag):
        if (isinstance(predicate_tag, PredicateSemanticTag)):
            self.predicates.append(predicate_tag)
        else:
            raise ValueError("The argument must be an instance of PredicateSemanticTag!")

