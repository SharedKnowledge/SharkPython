from PredicateSemanticTag import *

class SemanticNet:
    st_table = None
    predicates = None
    def __init__(self, st_table = None, predicates = None):
        if (st_table is None):
            self.st_table = {}
        else:
            self.st_table = st_table
        if (predicates is None):
            self.predicates = []
        else:
            self.predicates = predicates

    def add_tag(self, semantic_tag, semantic_tag_id):
        if (isinstance(semantic_tag, SemanticTag)):
            semantic_tag.id = semantic_tag_id
            self.st_table[semantic_tag_id] = semantic_tag
        else:
            raise ValueError("The argument must be an instance of SemanticTag!")

    def add_predicate(self, predicate_tag):
        if (isinstance(predicate_tag, PredicateSemanticTag)):
            self.predicates.append(predicate_tag)
        else:
            raise ValueError("The argument must be an instance of PredicateSemanticTag!")

