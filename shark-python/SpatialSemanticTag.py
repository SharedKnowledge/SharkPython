from SemanticTag import *
"""A SpatialSemanticTag represents a location in which a piece of information is relevant"""
class SpatialSemanticTag(SemanticTag):
    location = None #the relevant location
    def __init__(self, name, si, ewkt):
        SemanticTag.__init__(self, name, si)
        if ewkt is not None :
            self.location = ewkt
        else:
            raise ValueError("A SpatialSemanticTag needs at least one location! Otherwise please use a normal SemanticTag.")

    def __str__(self):
        return " [Name]: %s  [Si]: %s  [location]: %s" %(self.name, self.si, self.location)



