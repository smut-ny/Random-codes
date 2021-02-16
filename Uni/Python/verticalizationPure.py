
# 1) Napište program, který zadaný textový soubor tokenizuje a uloží jej do vertikály společně s informací o délce tokenu a odhadovaném počtu slabik (využijte již hotové funkce pro získávání informací o tokenu)

from textEdits import openFile
from textEdits import sylabesNum
import re

rawText = openFile('lyric.txt')

def verticalizationPure(rawText):
    vertical = ''
    for line in rawText:
        listItem = re.split('\W+', line)
        for word in listItem:
            if word:
                sylabes = pocetSlabik(word)
                vertical += word + sylabes +"\n"
    print(vertical)
    

verticalizationPure(rawText)