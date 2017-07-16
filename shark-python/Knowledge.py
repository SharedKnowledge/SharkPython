from Vocabulary import *
from InfoData import *
from InfoContent import *

class Knowledge:
    vocabulary = None
    info_data = None
    info_content = None
    def __init__(self, vocabulary, info_data, info_content):
        if (isinstance(vocabulary, Vocabulary)):
            self.vocabulary = vocabulary
        if (isinstance(info_data, InfoData)):
            self.info_data = info_data
        if (isinstance(info_content, InfoContent)):
            self.info_content = info_content





