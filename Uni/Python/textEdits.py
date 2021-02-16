
# Open txt file
def openFile(fileNameString):
    with open(fileNameString) as f:
        rawText = f.readlines()
    return rawText

# Returns number of sylabes

#ANCHOR TODO
#todo Learn something about it

def sylabesNum(word):
    sylabes = 0
    vocalList = ["a", "á", "e", "é", "i", "í", "o", "u", "ú", "ů", "l", "r", "y", "ě"]
    for character in word:
        if character.lower() in vocalList:
            sylabes += 1
    if len(word)/sylabes < 2.5:
        sylabes -= 1
    if len(word)/sylabes >= 3.5:
        sylabes += 1
    return print(sylabes)




sylabesNum("Kateřina")

