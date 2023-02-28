
# 3 letter combination of o,a,A,O - make each letter unique and different
letterBank = ['a','o','A','O']
possibilites = []

def makePossibilities(usedIndices, currAns):
    temp = usedIndices.copy()
    continuedAns = currAns

    for i in range(0, len(letterBank)):
        print("hi")
        if i in temp:
            continue
        continuedAns += letterBank[i]
        temp.append(i)
        if len(continuedAns) == 3:
            possibilites.append(continuedAns)
            break
        makePossibilities(temp, continuedAns)



def createCipher():
    # probably some recursion 
    retMonkeyCipher = {}



    return retMonkeyCipher

def decodeMonkeyCipher(currLegend, message): 
    #probably split message by 3 and use currLegend to add characters individually to decodedMessage
    decodedMessage = ""

    return decodedMessage

def main():
    empty = []
    answer = ""
    makePossibilities(empty, answer)
    print(possibilites)



main()