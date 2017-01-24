from PeerSemanticTag import  *
from PredicateSemanticTag import *


def main():
    address_max = Address("mail://s0123456@htw-berlin.de")
    address_maxima = Address("mail://s0123457@htw-berlin.de")
    peer_tag_max = PeerSemanticTag("Max Mustermann", "https://studi.f4.htw-berlin.de/~s0123456/", address_max)
    peer_tag_maxima = PeerSemanticTag("Maxima Mustermann", "https://studi.f4.htw-berlin.de/~s0123457/", address_maxima)
    predicate_tag = PredicateSemanticTag("Marriage", "https://en.wikipedia.org/wiki/Marriage", peer_tag_max.si, peer_tag_maxima.si)
    print("Predicate Tag:   " + predicate_tag.__str__())
    print("Max:"   + address_max.__str__())
    print("Maxima:"   + address_maxima.__str__())

if  __name__ =='__main__':main()