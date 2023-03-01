import random
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
    used = []
    # 65 - 90 is capitals (A-Z)
    # 97 - 122 is lowercase (a-z)
    retMonkeyCipher = {}

    for i in range(65, 91):
        choice = random.choice(possibilites)
        while choice not in used:
            choice = random.choice(possibilites)
            used.append(choice)

        retMonkeyCipher[ord(i)] = choice

    for i in range(97, 122):
        choice = random.choice(possibilites)
        while choice not in used:
            choice = random.choice(possibilites)
            used.append(choice)

        retMonkeyCipher[ord(i)] = choice

    return retMonkeyCipher

def decodeMonkeyCipher(currLegend, message): 
    #probably split message by 3 and use currLegend to add characters individually to decodedMessage
    decodedMessage = ""

    return decodedMessage

def main():
    empty = []
    answer = ""
    makePossibilities(answer)
    # print(possibilites)
    # print(len(possibilites))
    print(createCipher)



main()