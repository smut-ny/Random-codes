
import re

def openFile(path):
    with open(path) as f:
        rawText = f.read()
    return rawText


def getSyllabesCZ(word):
    vocals_konsonants = ""
    syllabes = len(word)
    vocals = ["a", "á", "e", "é", "i", "í", "o", "u", "ú", "ů", "l", "r", "y", "ě"]

    for character in word:
        if character.lower() in vocals:
            if character.lower() in "lr":
                vocals_konsonants += "W"
            else:
                vocals_konsonants += "V"
        else:
            vocals_konsonants += "K"
    
    #Syllabes/konsonants placeholder operations
    K = len(re.findall('K', vocals_konsonants))
    VV = len(re.findall('VV', vocals_konsonants))
    VWV = len(re.findall('VWV', vocals_konsonants))
    VW = len(re.findall('VW', vocals_konsonants))
    WV = len(re.findall('WV', vocals_konsonants))

    if K:
        syllabes -= K
    if VV:
        syllabes -= VV
    if VWV:
        syllabes -= VWV
    if VW:
        syllabes -= VW
    if WV:
        syllabes -= WV
    if WV and VW and VWV:
        syllabes += VWV 
        
    return syllabes


def getTokenizedList(plain_text):
    word = re.split('\W+', plain_text.lower())
    word = list(filter(None, word))
    return word