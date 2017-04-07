```javascript
# ASIP IoT BNF

# This document will describe the Backus-Naur form of the newly developed protocol ASIP IoT.
# This document is using Extended BNF nach ISO/IEC 14977. 

# Open Questions and TODOs: 
# - re-work adress definition -> more open definition of address names?
# - re-work times, maybe use https://www.w3.org/TR/xmlschema11-2/ for  duration · dateTime · time · date
# --- changes to utc and xmlschema 
# - re-work knowledge structure: infoData, infoSpace, infoMetaData
# - review vocabulary structure: semanticNet, stTable,  relations, property, semanticTagId 
# - clean up the terms: relations: predicates
# -- remove properties 
# -- stset = sttable 


## Basiscs

letter                  = 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G'
                        | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N'
                        | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U'
                        | 'V' | 'W' | 'X' | 'Y' | 'Z' | 'a' | 'b'
                        | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i'
                        | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p'
                        | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w'
                        | 'x' | 'y' | 'z' ;
digit                   = '0' | '1' | '2' | '3' | '4'
                        | '5' | '6' | '7' | '8' | '9' ;
number                  = digit {digit} ;
floatNumber             = number '.' number
character               = letter | digit ;
text                    = character {character} ;
bool                    = 'Y' | 'N' ;
void                    = '' ;

## ASIP-Message

message 				 = '{'
                            '"version":' floatNumber ','
                            '"encryptedKey":' text | void ','
                            '"sender":' peerSemanticTag ','
                            '"receiverTimes":' '[' timeSemanticTags ']' ','
							'"receiverPeers":' '[' peerSemanticTags ']' ','
							'"receiverLocations":' '[' spatialSemanticTags ']' ','
							'"receiverTopics":' '[' semanticTags ']' ','
                            '"ttl":' number','
                            '"content":' content
                          '}' signature ;
content                 = '{'
                            '"logicalSender":' logicalSender ','
                            insert | expose | raw
                          '}' signature ;
signature               = text ;
insert                  = '"insert":' '[' {knowledges} ']' ;
expose                  = '"expose":' '[' {interest} ']' ;
raw                     = '"raw":' text ;
logicalSender           = peerSemanticTag ;

## ASIP-SemanticTag

semanticTagName         = '"name":' name ;
name                    = text ;
semanticTagSI           = '"sis":' '[' {subjectIdentifiers} ']' ;
semanticTag             = '{'
                            semanticTagName ','
                            semanticTagSI
                          '}' ;
semanticTags            = semanticTag { ',' semanticTag } ;
peerSemanticTag         = '{'
                            semanticTagName ','
                            semanticTagSI ','
                            '"addresses":' '[' {addresses} ']'
                          '}' ;
peerSemanticTags        = peerSemanticTag { ',' peerSemanticTag } ;
spatialSemanticTag      = '{'
                            semanticTagName ','
                            semanticTagSI ','
                            '"locations":' '[' {locations} ']'
                          '}' ;
spatialSemanticTags     = spatialSemanticTag { ',' spatialSemanticTag } ;
timeSemanticTag         = '{'
                            semanticTagName ','
                            semanticTagSI ','
                            '"time":' '[' {time} ']'
                          '}' ;
timeSemanticTags        = timeSemanticTag { ',' timeSemanticTag } ;
subjectIdentifiers      = subjectIdentifier { ',' subjectIdentifier } ;
subjectIdentifier       = uri ;
uri                     = '"uri":' http://www.w3.org/Addressing/URL/5_URI_BNF.html ;
address                 = '{'
                            '"address":' gcf
                          '}' ;
addresses               = address | { ',' address } ;
## TODO discuss addresses
gcf                     = tcpEndpoint | httpEndpoint | mailEndpoint ;
endPoint                = ( character | '.' | '-' ) { ( character | '.' | '-' ) } ;
port                    = number ;
tcpEndpoint             = 'tcp' '://' endPoint [ ':' port ] ;
httpEndpoint            = 'http' '://' endPoint [ ':' port ] ;
mailEndpoint            = 'mail' '://' user '@' endPoint [ ';' mbSize ] ;
user                    = text
mbSize                  = number ;
locations               = location { ',' location } ;
location                = '{'
                            '"location":' ewkt
                          '}' ;
ewkt                    = defined at:
                          http://docs.opengeospatial.org/is/12-063r5/12-063r5.html ;
## TODO: re-work times  
times                    = '{'
                            '"format":' xmlschema | utcTime ','
							duration | period 
                          '}' ;
utcTime                 = '"utcTime":' https://www.ietf.org/rfc/rfc3339.txt Part 5.6 ;
xmlschema				= '"xmlschema":' https://www.w3.org/TR/xmlschema11-2/ ;
duration 				= '"duration":' text ',' '"startTime":' text ;
period					= '"period":' text ',' '"interval":' text ;

## ASIP-Commands

### Insert


knowledge               = '{'
                            '"vocabulary":' vocabulary ','
                            '"infoData":' '[' infoDatas ']' ','
                            infoContent
                          '}' ;
knowledges              = knowledge { ',' knowledge } ;
infoData                = '{'
                            '"infoSpace":' infoSpace ','
                            '"infoMetaData":' '[' [infoMetaDatas] ']'
                          '}' ;
infoDatas               = infoData { ',' infoData } ;
infoMetaData            = '{'
                            '"name": ' text ','
                            '"offset":' number ','
                            '"length":' number
                          '}' ;
infoMetaDatas           = infoMetaData { ',' infoMetaData } ;              
infoContent             = '{'
                            '"byteStream":' text
                          '}' ;
infoSpace               = '{'
                            '"topics":' [ semanticTags ] ','
                            '"types":' [ semanticTags ] ','
                            '"approvers":' [ peerSemanticTags ] ','
                            '"sender":' [ peerSemanticTag ]','
                            '"recipients":' [ peerSemanticTags ] ','
                            '"locations":' [ spatialSemanticTags ] ','
                            '"times":' [ timeSemanticTags ]
                          '}' ;

// TODO: Check Vocabulary
vocabulary              = '{'
                            topicDim ','
                            typeDim ','
                            peerDim ','
                            locationDim ','
                            timeDim
                          '}' ;
topicDim                = semanticNet ;
typeDim                 = semanticNet ;
peerDim                 = peerSemanticTagNet ;
locationDim             = spatialSemanticTagNet ;
timeDim                 = timeSemanticTagNet ;

// TODO: Check SemanticNets
semanticNet             = '{'
                            '"stTable":' '['
                              { semanticTagId ',' semanticTag } ','
                            '"relations":' '[' {predicate} ']'
                          '}' ;
peerSemanticNet         = '{'
                            '"stTable":' '['
                              { semanticTagId ',' peerSemanticTag }
                             ']' ','
                            '"relations":' '[' { predicate} ']'
                          '}' ;
spatialSemanticNet      = '{'
                            '"stTable":' '['
                              { semanticTagId ',' spatialSemanticTag }
                            ']' ','
                            '"relations":' '[' {predicate} ']'
                          '}' ;
timeSemanticNet         = '{'
                            '"stTable":' '['
                              { semanticTagId ',' timeSemanticTag }
                            ']' ','
                            '"relations":' '[' { predicate} ']'
                          '}' ;
semanticTagId           = '{' '"id":' text '}' ;
predicate                = '{'
                            '"name":' text
                            '"sourceId":' text
                            '"targetId":' text
                          '}' ;

### Expose

interest                = '{'
                            '"topics":' '[' {semanticTags} | void ']' ','
                            '"types":' '[' {semanticTags} | void ']' ','
                            '"approvers":' '[' {peerSemanticTags} | void ']' ','
                            '"sender":' peerSemanticTag | void ','
                            '"recipients":' '[' {peerSemanticTags} | void ']' ','
                            '"locations":' '[' {spatialSemanticTags} | void ']' ','
                            '"times":' '[' {timeSemanticTags} | void ']' ','
                            '"direction":' 'IN' | 'OUT' | 'INOUT' | 'NO' '}'
                          '}' ;
interests               = interest { ',' interest } ;

```