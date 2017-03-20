
class Interest:
    topics = None
    types = None
    approvers = None
    sender = None
    recipients = None
    locations = None
    times = None
    predicates = None
    direction = None
    def __init__(self, topics, types, approvers, sender, recipients, locations, times, predicates, direction):
        self.topics = topics
        self.types = types
        self.approvers = approvers
        self.sender = sender
        self.recipients = recipients
        self.locations = locations
        self.times = times
        self.predicates = predicates
        self.direction = direction




