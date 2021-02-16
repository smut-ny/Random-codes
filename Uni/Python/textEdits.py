
import re

# Open txt file
def openFile(fileNameString):
    with open(fileNameString) as f:
        rawText = f.readlines()
    return rawText

# Returns number of sylabes

def sylabesNumCZ(word):
    vocKonsonants = ""
    sylabes = len(word)
    vocalList = ["a", "á", "e", "é", "i", "í", "o", "u", "ú", "ů", "l", "r", "y", "ě"]
    for character in word:
        if character.lower() in vocalList:
            if character.lower() in "lr":
                vocKonsonants += "W"
            else:
                vocKonsonants += "V"
        else:
            vocKonsonants += "K"
    
    K = len(re.findall('K', vocKonsonants))
    VV = len(re.findall('VV', vocKonsonants))
    VWV = len(re.findall('VWV', vocKonsonants))
    VW = len(re.findall('VW', vocKonsonants))
    WV = len(re.findall('WV', vocKonsonants))

    if K:
        sylabes -= K
    if VV:
        sylabes -= VV
    if VWV:
        sylabes -= VWV
    if VW:
        sylabes -= VW
    if WV:
        sylabes -= WV
    if WV and VW and VWV:
        sylabes += VWV * 2
        
    #Sylabes and Konsonants operations
    return sylabes

