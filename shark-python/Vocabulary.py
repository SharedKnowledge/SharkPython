from SemanticNet import *

class Vocaulary:
    topic_dim = None
    type_dim = None
    peer_dim = None
    location_dim = None
    time_dim = None

    def __init__(self, topic_dim):
        if (isinstance(topic_dim, SemanticNet)):
            self.topic_dim = topic_dim
        else:
            raise ValueError("The argument must be an instance of SemanticNet!")



