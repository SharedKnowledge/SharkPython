from PredicateSemanticTag import *

class SemanticNet:
    st_table = None
    predicates = None
    def __init__(self, st_table = None, predicates = None):
        if (st_table is None):
            self.st_table = dict(int, SemanticTag)
        else:
            self.st_table = st_table
        if (predicates is None):
            self.predicates = []
        else:
            self.predicates = predicates

    def add_Tag(self, semantic_tag):
        if (isinstance(semantic_tag, SemanticTag)):
            self.st_table.append(semantic_tag)
        else:
            raise ValueError("The argument must be an instance of SemanticTag!")

    def add_predicate(self, predicate_tag):
        if (isinstance(predicate_tag, PredicateSemanticTag)):
            self.predicates.append(predicate_tag)
        else:
            raise ValueError("The argument must be an instance of PredicateSemanticTag!")

