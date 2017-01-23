from SemanticTag import *

class PeerSemanticTag(SemanticTag):
    addresses = None
    def __init__(self, name, si, addresses):
        SemanticTag.__init__(self, name, si)
        if addresses:
            self.addresses = addresses
        else:
            raise ValueError("A PeerSemanticTag needs at least one address! Otherwise please use a normal SemanticTag.")

    def __str__(self):
        return " [Name]: %s  [Si]: %s  [addresses]: %s" %(self.name, self.si, self.addresses)


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
        return " [Address]: %s" %(self.endpoint)




def main():
    tag = PeerSemanticTag("Dustin Feurich", "https://studi.f4.htw-berlin.de/~s0540042/", "s0540042@htw-berlin.de")
    print("Generated Tag: " + tag.__str__())
    address = Address("mail://s0540042@htw-berlin.de")
    print(address)



if  __name__ =='__main__':main()