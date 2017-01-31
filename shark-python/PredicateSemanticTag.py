from SemanticTag import *

class PredicateSemanticTag(SemanticTag):
    source_si = None
    target_si = None
    def __init__(self, name, si, source_si, target_si):
        SemanticTag.__init__(self, name, si)
        if source_si and target_si:
            self.source_si = source_si
            self.target_si = target_si
        else:
            raise ValueError("A PredicateSemanticTag needs a source and target si! Otherwise please use a normal SemanticTag.")

    def __str__(self):
        return " [Name]: %s  [Si]: %s  [source_si]: %s  [target_si] %s" %(self.name, self.si, self.source_si, self.target_si)

def main():
    tag = PredicateSemanticTag("Marriage", "https://en.wikipedia.org/wiki/Marriage", "max.muster@htw-berlin.de", "maxima.muster@htw-berlin.de")
    print("Generated PredicateTag: " + tag.__str__())
    #tag_invalid = PredicateSemanticTag("Invalid", "www.example.org", None, None)


if  __name__ =='__main__':main()