
# 1) Napište program, který zadaný textový soubor tokenizuje a uloží jej do vertikály společně s informací o délce tokenu a odhadovaném počtu slabik (využijte již hotové funkce pro získávání informací o tokenu)

#TODO Vkládat importy do funkce nebo ne?
# TODO Jakým způsobem si program vyčistit? Používat více files? Jak na moduly importy?
from textEdits import openFile
from textEdits import sylabesNumCZ
import re

rawText = openFile('lyric.txt')

def verticalizationPure(rawText):
    vertical = ''
    for line in rawText:
        listItem = re.split('\W+', line)
        for word in listItem:
            if word:
                sylabes = sylabesNumCZ(word)
                vertical += word + " | tok: " + str(len(word)) + " syl: " + str(sylabes) + "\n"
    return vertical