from SemanticNet import *
from PeerSemanticNet import *
from TimeSemanticNet import *
from SpatialSemanticNet import *
"""The vocaulary contains every Tag that the executing machine has inside its KnowledgeBase. 
The Tags are stored in their respective SemanticNets"""
class Vocabulary:
    topic_dim = None #A SemanticNet with SemanticTags and PredicateSemanticTags
    type_dim = None #A SemanticNet with SemanticTags and PredicateSemanticTags
    peer_dim = None #A PeerSemantic Net with PeerSemanticTags and PredicateSemanticTags
    location_dim = None #A SpatialSemantic Net with SpatialSemanticTags and PredicateSemanticTags
    time_dim = None #A TimeSemantic Net with TimeSemanticTags and PredicateSemanticTags

    def __init__(self):
        pass

    def __init__(self, topic_dim, type_dim, peer_dim, location_dim, time_dim):
        if (isinstance(topic_dim, SemanticNet) or isinstance(type_dim, SemanticNet)
            or isinstance(peer_dim, PeerSemanticNet) or isinstance(location_dim, SpatialSemanticNet)
            or isinstance(time_dim, TimeSemanticNet)):
            self.topic_dim = topic_dim
            self.type_dim = type_dim
            self.peer_dim = peer_dim
            self.location_dim = location_dim
            self.time_dim = time_dim
        else:
            raise ValueError("At least one argument was invalid!")


    def __str__(self):
        return " [Topic Dimension]: %s  \n[Type Dimention]: %s  \n[Peer Dimension]: %s  " \
               "\n[Location Dimension]: %s  \n[Time Dimension]: %s" \
               %(self.topic_dim, self.type_dim, self.peer_dim, self.location_dim, self.time_dim)



