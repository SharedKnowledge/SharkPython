from Interest import  *


class KnowledgeBase(object):
    knowledge = None
    vocabulary = None

    def __init__(self, knowledge, vocabulary):
        if knowledge:
            self.knowledge = knowledge
        if vocabulary:
            self.vocabulary = vocabulary

    def expose(self, interest):
        if interest is not None and isinstance(interest, Interest):
            pass





    def insert(self, knowledge):
        pass