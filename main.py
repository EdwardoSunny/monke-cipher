
# 3 letter combination of o,a,A,O - make each letter unique and different
letterBank = ['a','o','A','O']
possibilites = []

def makePossibilities(currAns): #recursively make stuff
    print("-------")
    # print(usedIndices)
    # print(currAns)

    for i in range(0, len(letterBank)):
        
        continuedAns = currAns
        
        continuedAns += letterBank[i]

        print(continuedAns)

        if len(continuedAns) == 3:
            if continuedAns not in possibilites:
                possibilites.append(continuedAns)
                continue
        
        makePossibilities(continuedAns)



def createCipher():
    
    retMonkeyCipher = {}



    return retMonkeyCipher

def decodeMonkeyCipher(currLegend, message): 
    #probably split message by 3 and use currLegend to add characters individually to decodedMessage
    decodedMessage = ""

    return decodedMessage

def main():
    empty = []
    answer = ""
    makePossibilities(answer)
    print(possibilites)
    print(len(possibilites))



main()