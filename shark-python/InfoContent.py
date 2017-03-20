
class InfoContent:
    byte_stream = None
    def __init__(self, byte_stream):
        if (byte_stream is None):
            raise ValueError("A InfoContent needs a bytestream!")
        else:
            self.byte_stream = byte_stream




