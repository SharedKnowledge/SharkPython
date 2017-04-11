from Interest import  *


class KnowledgeBase(object):
    knowledge = None


    def __init__(self, knowledge):
        if knowledge:
            self.knowledge = knowledge

    def expose(self, interest):
        if interest is not None and isinstance(interest, Interest):
            pass





    def insert(self, knowledge):
        if (knowledge.vocabulary is not None):
            if (knowledge.vocabulary.topic_dim is not None):
                insert_tags = knowledge.vocabulary.topic_dim.st_table.values()
                kb_tags = self.knowledge.vocabulary.topic_dim.st_table.values()
                new_tags = [x for x in insert_tags if x not in kb_tags] # make use of overwritten equals method (__eq__) in SemanticTag.py
                for tag in new_tags:
                    self.knowledge.vocabulary.topic_dim.add_tag(tag, tag.id)
                new_predicates = [x for x in knowledge.vocabulary.topic_dim.predicates if x not in self.knowledge.vocabulary.topic_dim.predicates] # make use of overwritten equals method (__eq__) in PredicateSemanticTag.py
                for predicate in new_predicates:
                    self.knowledge.vocabulary.topic_dim.add_predicate(predicate)

            #Repeat the first block for the other dimensions (after intensive testing)
            if (knowledge.vocabulary.type_dim is not None):
                pass
            if (knowledge.vocabulary.peer_dim is not None):
                pass
            if (knowledge.vocabulary.location_dim is not None):
                pass
            if (knowledge.vocabulary.time_dim is not None):
                pass














