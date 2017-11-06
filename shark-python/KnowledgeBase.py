import Interest
from Knowledge import Knowledge, Vocabulary, SemanticNet

"""The KnowledgeBase includes all known Tags, Semantic Nets and Predicates of the Peer
It offers methods for inserting new Knowledge into the Knowledge Base or for
exposing an interest to another KnowledgeBase"""
class KnowledgeBase(object):
    knowledge = None


    def __init__(self, knowledge):
        if knowledge:
            self.knowledge = knowledge

    """Dependent on the merge status this method inserts new Knowledge into the KnowledgeBase."""
    def insert(self, knowledge, merge_status = 2): #default merge status is status 2
        if (knowledge.vocabulary is not None):
            if (knowledge.vocabulary.topic_dim is not None):
                self.process_insert(knowledge.vocabulary.topic_dim, self.knowledge.vocabulary.topic_dim, merge_status)
            if (knowledge.vocabulary.type_dim is not None):
                self.process_insert(knowledge.vocabulary.type_dim, self.knowledge.vocabulary.type_dim, merge_status)
            if (knowledge.vocabulary.peer_dim is not None):
                self.process_insert(knowledge.vocabulary.peer_dim, self.knowledge.vocabulary.peer_dim, merge_status)
            if (knowledge.vocabulary.location_dim is not None):
                self.process_insert(knowledge.vocabulary.location_dim, self.knowledge.vocabulary.location_dim, merge_status)
            if (knowledge.vocabulary.time_dim is not None):
                self.process_insert(knowledge.vocabulary.time_dim, self.knowledge.vocabulary.time_dim, merge_status)

    def process_insert(self, dimension_insert, dimension_kb, merge_status):
        insert_tags = dimension_insert.st_table.values()
        kb_tags = dimension_kb.st_table.values()
        if (merge_status == 0): #status 0: add all tags of the new inserting knowledge to the KnowledgeBase
            new_tags = insert_tags
        elif (merge_status >= 1): #status >=1: add only the tags which are yet unknown to the KnowledgeBase; already known tags are later processed if the merge status is 2 or 3
            new_tags = [x for x in insert_tags if x not in kb_tags]
        else:
            new_tags = []
        for tag in new_tags:
            dimension_kb.add_tag(tag, tag.id + 100)
        if (merge_status == 2): #status 2: replace already known tags of the KnowledgeBase with the tags of the inserting knowledge
            known_tags = [x for x in insert_tags if x in kb_tags]
            for tag in known_tags:
                dimension_kb.replace_tag(tag)
        if (merge_status == 3): #status3: merge already known tags of the KnowledgeBase with the tags of the inserting knowledge
            known_tags = [x for x in insert_tags if x in kb_tags]
            for tag in known_tags:
                dimension_kb.merge_tag(tag)

        new_predicates = [x for x in dimension_insert.predicates if x not in dimension_kb.predicates] #add new predicates to the KnowledgeBase
        for predicate in new_predicates:
            self.knowledge.vocabulary.topic_dim.add_predicate(predicate)


    def expose(self, interest, relations = False):
        knowledge = Knowledge()
        vocabulary = Vocabulary()
        topic_dimension = SemanticNet()
        if interest is not None and isinstance(interest, Interest):
            if (interest.topics is not None):
                tags = [x for x in interest.topics if x in self.knowledge.vocabulary.topic_dim.st_table.values()]
                for tag in tags:
                    topic_dimension.add_tag(tag, tag.id) #Add all tags which are relevant according to the interest
                    if (relations):
                        for relation in self.knowledge.vocabulary.topic_dim.predicates:
                            if (relation.source_si == tag.si or relation.target_si == tag.si):
                                topic_dimension.add_predicate(relation) #add all predicates which are targetting already added tags
                vocabulary.topic_dim = topic_dimension

        knowledge.vocabulary = vocabulary
        return knowledge

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i > 0:
            raise StopIteration
        else:
            self.i += 1
            return self

























