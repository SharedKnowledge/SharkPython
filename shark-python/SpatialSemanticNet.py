from PredicateSemanticTag import *
from SpatialSemanticTag import *

class SpatialSemanticNet:
    sst_table = None
    predicates = None
    def __init__(self, sst_table = None, predicates = None):
        if (sst_table is None):
            self.sst_table = {}
        else:
            self.sst_table = sst_table
        if (predicates is None):
            self.predicates = []
        else:
            self.predicates = predicates

    def add_Tag(self, spatial_semantic_tag, semantic_tag_id):
        if (isinstance(spatial_semantic_tag, SpatialSemanticTag)):
            self.sst_table[semantic_tag_id] = spatial_semantic_tag
        else:
            raise ValueError("The argument must be an instance of SpatialSemanticTag!")

    def add_predicate(self, predicate_tag):
        if (isinstance(predicate_tag, PredicateSemanticTag)):
            self.predicates.append(predicate_tag)
        else:
            raise ValueError("The argument must be an instance of PredicateSemanticTag!")

