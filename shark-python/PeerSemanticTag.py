from SemanticTag import *
"""A SpatialSemanticTag represents a person or a device, which is relevant to the piece of information"""
class PeerSemanticTag(SemanticTag):
    address = None #The address of the Peer has to be an object of type Address
    def __init__(self, name, si, address):
        SemanticTag.__init__(self, name, si)
        if isinstance(address, Address) :
            self.address = address
        else:
            raise ValueError("A PeerSemanticTag needs at least one address! Otherwise please use a normal SemanticTag.")

    def __str__(self):
        return " [Name]: %s  [Si]: %s  [address]: %s" %(self.name, self.si, self.address)


class Address: #A valid address of the peer can be a tcp IP, an email or a http internet address
    tcp = False
    email = False
    http= False
    endpoint = None
    def __init__(self, address):
        if address is not None and isinstance(address, str):
            if "tcp://" in address:
                self.tcp = True
            elif "mail://" in address:
                self.email = True
            elif "http://" in address:
                self.http = True
            else:
                raise ValueError("The address has to be tcp, mail or http!")
            self.endpoint = address
        else:
            raise ValueError()

    def __str__(self):
        return "%s" %(self.endpoint)
