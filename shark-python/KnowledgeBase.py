from Interest import  *
from Knowledge import Knowledge, Vocabulary, SemanticNet


class KnowledgeBase(object):
    knowledge = None


    def __init__(self, knowledge):
        if knowledge:
            self.knowledge = knowledge

    def insert(self, knowledge, merge_status = 2):
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
        if (merge_status == 0):
            new_tags = insert_tags
        elif (merge_status >= 1):
            new_tags = [x for x in insert_tags if x not in kb_tags]
        else:
            new_tags = []
        for tag in new_tags:
            dimension_kb.add_tag(tag, tag.id + 100)
        if (merge_status == 2):
            known_tags = [x for x in insert_tags if x in kb_tags]
            for tag in known_tags:
                dimension_kb.replace_tag(tag)
        if (merge_status == 3):
            known_tags = [x for x in insert_tags if x in kb_tags]
            for tag in known_tags:
                dimension_kb.merge_tag(tag)

        new_predicates = [x for x in dimension_insert.predicates if x not in dimension_kb.predicates]
        for predicate in new_predicates:
            self.knowledge.vocabulary.topic_dim.add_predicate(predicate)


    def expose(self, interest, relations = False):
        knowledge = Knowledge()
        vocabulary = Vocabulary()
        topic_dimension = SemanticNet()
        if interest is not None and isinstance(interest, Interest): #Todo: Dies noch für die anderen Dimensionen analog hinzufügen, am besten wie beim insert aufteilen
            if (interest.topics is not None):
                tags = [x for x in interest.topics if x in self.knowledge.vocabulary.topic_dim.st_table.values()]
                for tag in tags:
                    topic_dimension.add_tag(tag, tag.id)
                    if (relations):
                        for relation in self.knowledge.vocabulary.topic_dim.predicates:
                            if (relation.source_si == tag.si or relation.target_si == tag.si):
                                topic_dimension.add_predicate(relation)
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

























