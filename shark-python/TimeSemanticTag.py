from SemanticTag import *
"""A TimeSemanticTag represents a time period in which a piece of information is relevant"""
class TimeSemanticTag(SemanticTag):
    time = None #the starting time of the time period
    duration = None #the duration of the time period
    def __init__(self, name, si, time, duration):
        SemanticTag.__init__(self, name, si)
        if time is not None and duration is not None:
            self.time = time
            self.duration = duration
        else:
            raise ValueError("A TimeSemanticTag needs a time specification and a time duration! Otherwise please use a normal SemanticTag.")

    def __str__(self):
        return " [Name]: %s  [Si]: %s  [location]: %s" %(self.name, self.si, self.location)



