from PredicateSemanticTag import *
"""A SemanticNet is a container for Semantic Tags. Contrary to simple Tag Sets, Relations can also be added between two
Semantic Tags."""

class SemanticNet:
    st_table = None #The Semantic Tags
    predicates = None #The relations/predicates
    def __init__(self, st_table = None, predicates = None):
        if (st_table is None):
            self.st_table = {} #The Tags are stored within a dictionary
        else:
            self.st_table = st_table
        if (predicates is None):
            self.predicates = [] #The relations are stored within a list
        else:
            self.predicates = predicates

    def add_tag(self, semantic_tag, semantic_tag_id):
        if (isinstance(semantic_tag, SemanticTag)):
            semantic_tag.id = semantic_tag_id
            self.st_table[semantic_tag_id] = semantic_tag #The tags are added to the dictionary with a key, which is either the id of the tag or an arbitrary unique id
        else:
            raise ValueError("The argument must be an instance of SemanticTag!")

    def remove_tag(self, semantic_tag, semantic_tag_id):
        if (isinstance(semantic_tag, SemanticTag)):
            del self.st_table[semantic_tag_id] #The tags are removed from the dictionary with a key, which is either the id of the tag or an arbitrary unique id
        else:
            raise ValueError("The argument must be an instance of SemanticTag!")

    def replace_tag(self, semantic_tag):
        if (isinstance(semantic_tag, SemanticTag)):
            for tag in self.st_table.values():
                if (semantic_tag == tag): #Note: the equality method of the class Semantic Tag is overwritten
                    self.remove_tag(tag, tag.id)
                    self.add_tag(semantic_tag, semantic_tag.id)
        else:
            raise ValueError("The argument must be an instance of SemanticTag!")

    def merge_tag(self, semantic_tag):
        if (isinstance(semantic_tag, SemanticTag)):
            for tag in self.st_table.values():
                if (semantic_tag == tag):
                    tag.si.append(semantic_tag.si) #Tags are beeing merged with the merging of all SIs of the two Tags
        else:
            raise ValueError("The argument must be an instance of SemanticTag!")


    def add_predicate(self, predicate_tag):
        if (isinstance(predicate_tag, PredicateSemanticTag)):
            self.predicates.append(predicate_tag) #Target and source Tag of the relation/predicate are already stored in the PredicateTag
        else:
            raise ValueError("The argument must be an instance of PredicateSemanticTag!")

    def remove_predicate(self, predicate_tag):
        if (isinstance(predicate_tag, PredicateSemanticTag)):
            self.predicates.remove(predicate_tag)
        else:
            raise ValueError("The argument must be an instance of PredicateSemanticTag!")

