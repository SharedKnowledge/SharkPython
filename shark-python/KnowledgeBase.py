from Interest import  *


class KnowledgeBase(object):
    knowledge = None


    def __init__(self, knowledge):
        if knowledge:
            self.knowledge = knowledge

    def insert(self, knowledge, conflict_resolution = 2):
        if (knowledge.vocabulary is not None):
            if (knowledge.vocabulary.topic_dim is not None):
                self.process_insert(knowledge.vocabulary.topic_dim, self.knowledge.vocabulary.topic_dim, conflict_resolution)
            if (knowledge.vocabulary.type_dim is not None):
                self.process_insert(knowledge.vocabulary.type_dim, self.knowledge.vocabulary.type_dim, conflict_resolution)
            if (knowledge.vocabulary.peer_dim is not None):
                self.process_insert(knowledge.vocabulary.peer_dim, self.knowledge.vocabulary.peer_dim, conflict_resolution)
            if (knowledge.vocabulary.location_dim is not None):
                self.process_insert(knowledge.vocabulary.location_dim, self.knowledge.vocabulary.location_dim, conflict_resolution)
            if (knowledge.vocabulary.time_dim is not None):
                self.process_insert(knowledge.vocabulary.time_dim, self.knowledge.vocabulary.time_dim, conflict_resolution)

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
            dimension_kb.add_tag(tag, tag.id)
        if (merge_status == 2):
            known_tags = [x for x in insert_tags if x in kb_tags]
            for tag in known_tags:
                dimension_kb.replace_tag(tag)

        new_predicates = [x for x in dimension_insert.predicates if x not in dimension_kb.predicates]
        for predicate in new_predicates:
            self.knowledge.vocabulary.topic_dim.add_predicate(predicate)


    def expose(self, interest):
        if interest is not None and isinstance(interest, Interest):
            pass














