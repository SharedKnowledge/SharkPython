from PredicateSemanticTag import *
from SpatialSemanticTag import *
"""A SpatialSemanticNet is a container for SpatialSemanticTags. Contrary to simple Tag Sets, Relations can also be added between two
SpatialSemanticTags."""
class SpatialSemanticNet:
    sst_table = None #The PeerSemanticTags
    predicates = None #The relations/predicates
    def __init__(self, sst_table = None, predicates = None):
        if (sst_table is None):
            self.sst_table = {} #The Tags are stored within a dictionary
        else:
            self.sst_table = sst_table
        if (predicates is None):
            self.predicates = [] #The relations are stored within a list
        else:
            self.predicates = predicates

    def add_Tag(self, spatial_semantic_tag, semantic_tag_id):
        if (isinstance(spatial_semantic_tag, SpatialSemanticTag)):
            self.sst_table[semantic_tag_id] = spatial_semantic_tag #The tags are added to the dictionary with a key, which is either the id of the tag or an arbitrary unique id
        else:
            raise ValueError("The argument must be an instance of SpatialSemanticTag!")

    def remove_tag(self, semantic_tag, semantic_tag_id):
        if (isinstance(semantic_tag, SpatialSemanticTag)):
            del self.st_table[semantic_tag_id] #The tags are removed from the dictionary with a key, which is either the id of the tag or an arbitrary unique id
        else:
            raise ValueError("The argument must be an instance of SpatialSemanticTag!")


    def replace_tag(self, semantic_tag):
        if (isinstance(semantic_tag, SpatialSemanticTag)):
            for tag in self.st_table.values():
                if (semantic_tag == tag): #Note: the equality method of the class Semantic Tag is overwritten
                    self.remove_tag(tag, tag.id)
                    self.add_tag(semantic_tag, semantic_tag.id)
        else:
            raise ValueError("The argument must be an instance of SpatialSemanticTag!")

    def merge_tag(self, semantic_tag):
        if (isinstance(semantic_tag, SpatialSemanticTag)):
            for tag in self.st_table.values():
                if (semantic_tag == tag):
                    tag.si.append(semantic_tag.si) #Tags are beeing merged with the merging of all SIs of the two Tags
        else:
            raise ValueError("The argument must be an instance of SpatialSemanticTag!")

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



