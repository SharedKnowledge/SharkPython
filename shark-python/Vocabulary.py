from SemanticNet import *
from PeerSemanticNet import *
from TimeSemanticNet import *
from SpatialSemanticNet import *

class Vocabulary:
    topic_dim = None
    type_dim = None
    peer_dim = None
    location_dim = None
    time_dim = None

    #Todo: Konstruktor sicherer machen
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



