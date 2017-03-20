from InfoSpace import *
from InfoMetaData import *

class InfoData:
    info_space = None
    info_meta_data = None
    def __init__(self, info_space, info_meta_data):
        if (info_space is not None and isinstance(info_space, InfoSpace) ):
            self.info_space = info_space
        if (info_meta_data is not None and isinstance(info_meta_data, InfoMetaData) ):
            self.info_meta_data = info_meta_data




