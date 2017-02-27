from PredicateSemanticTag import *
from TimeSemanticTag import *

class TimeSemanticNet:
    tst_table = None
    predicates = None
    def __init__(self, tst_table = None, predicates = None):
        if (tst_table is None):
            self.tst_table = {}
        else:
            self.tst_table = tst_table
        if (predicates is None):
            self.predicates = []
        else:
            self.predicates = predicates

    def add_Tag(self, time_semantic_tag, semantic_tag_id):
        if (isinstance(time_semantic_tag, TimeSemanticTag)):
            self.tst_table[semantic_tag_id] = time_semantic_tag
        else:
            raise ValueError("The argument must be an instance of TimeSemanticTag!")

    def add_predicate(self, predicate_tag):
        if (isinstance(predicate_tag, PredicateSemanticTag)):
            self.predicates.append(predicate_tag)
        else:
            raise ValueError("The argument must be an instance of PredicateSemanticTag!")

