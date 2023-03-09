import random
# 3 letter combination of o,a,A,O - make each letter unique and different
letterBank = ['a','o','A','O']
possibilites = []

def makePossibilities(currAns): #recursively make stuff
    # print("-------")
    # print(usedIndices)
    # print(currAns)

    for i in range(0, len(letterBank)):
        
        continuedAns = currAns
        
        continuedAns += letterBank[i]

        # print(continuedAns)

        if len(continuedAns) == 3:
            if continuedAns not in possibilites:
                possibilites.append(continuedAns)
                continue
        
        makePossibilities(continuedAns)



def createCipher():
    used = []
    # 65 - 90 is capitals (A-Z)
    # 97 - 122 is lowercase (a-z)
    retMonkeyCipher = {}

    for i in range(65, 91):
        choice = random.choice(possibilites)
        while choice in used:
            choice = random.choice(possibilites)
        
        used.append(choice)

        retMonkeyCipher[chr(i)] = choice

    for i in range(97, 123):
        choice = random.choice(possibilites)
        while choice in used:
            choice = random.choice(possibilites)
        
        used.append(choice)

        retMonkeyCipher[chr(i)] = choice

    return retMonkeyCipher

def decodeMonkeyCipher(currLegend, message): 
    #probably split message by 3 and use currLegend to add characters individually to decodedMessage
    decodedMessage = ""

    return decodedMessage

def writeLegend(dict):
    with open('legend.txt', 'w') as f:
        for keys, values in dict.items():
            f.write("" + keys + "," + values + "\n")
    
    f.close()

def readLegend():
    f = open('legend.txt', 'r')
    


def createCipherMessage(currLegend, message):
    ret = ""

    for i in message:
        if i in currLegend.keys():
            ret += currLegend[i]
        else:
            ret += i
    return ret

def main():
    
    answer = ""
    makePossibilities(answer)
    # print(possibilites)
    # print(len(possibilites))
    # print(createCipher)
    dict = createCipher()
    print(dict)
    writeLegend(dict)


main()