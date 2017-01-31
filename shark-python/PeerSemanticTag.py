from SemanticTag import *

class PeerSemanticTag(SemanticTag):
    address = None
    def __init__(self, name, si, address):
        SemanticTag.__init__(self, name, si)
        if isinstance(address, Address) :
            self.address = address
        else:
            raise ValueError("A PeerSemanticTag needs at least one address! Otherwise please use a normal SemanticTag.")

    def __str__(self):
        return " [Name]: %s  [Si]: %s  [address]: %s" %(self.name, self.si, self.address)


class Address:
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




def main():
    address = Address("mail://s0540042@htw-berlin.de")
    print(address)
    tag = PeerSemanticTag("Dustin Feurich", "https://studi.f4.htw-berlin.de/~s0540042/", address)
    print("Generated Tag: " + tag.__str__())




if  __name__ =='__main__':main()