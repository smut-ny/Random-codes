# 1) Vytvořte vlastní funkci AbsolutniHodnota, která pro zadané číslo vrátí jeho absolutní hodnotu (bez použití funkce abs)
def absolutniHodnota(number):
  if number >= 0:
    return number
  else:
    return number * -1

#[x]
print(absolutniHodnota(-151987651))
print(absolutniHodnota(425254254))
print(absolutniHodnota(0))
print(absolutniHodnota(-123))
print(absolutniHodnota(-1))
print(absolutniHodnota(1))
print(absolutniHodnota(456489))
print(absolutniHodnota(422243))
print(absolutniHodnota(-12313.58))
print(absolutniHodnota(1.58))
print(absolutniHodnota(-2.598526))
print(absolutniHodnota(-8))

# 2) Funkce Nejvetsi, která ze 2 čísel vrátí to nejvyšší
def nejvetsi(numberOne, numberTwo):
  if numberOne > numberTwo:
    return numberOne
  elif numberOne == numberTwo:
    return "Numbers are equal"
  else:
    return numberTwo

#[x] 
print(nejvetsi(1, 8))
print(nejvetsi(-46465456, 4561))
print(nejvetsi(2523, 22))
print(nejvetsi(1.258, 8.2))
print(nejvetsi(1.231, 0.1))
print(nejvetsi(80, 0))
print(nejvetsi(0, -8))
print(nejvetsi(1000006123, 81551511515))
print(nejvetsi(2, 2))


# 3) Funkce pojmenovaná Nejvetsi3, která ze 3 čísel vrátí nejvyšší
def nejvetsi3(numberOne, numberTwo, numberThree):
  if (numberOne > numberTwo) and (numberOne > numberThree):
    return numberOne
  elif (numberTwo > numberOne) and (numberTwo > numberThree):
    return numberTwo
  elif (numberThree > numberOne) and (numberThree > numberOne):
    return numberThree
  else:
    return "All three numbers are equal: %s" % numberOne

#[x]
print(nejvetsi3(1, 2, 3))
print(nejvetsi3(2, 1, 3))
print(nejvetsi3(3, 2, 1))
print(nejvetsi3(1, 1, 2))
print(nejvetsi3(1, 2, 1))
print(nejvetsi3(2, 1, 1))
print(nejvetsi3(0, 0, 0))
print(nejvetsi3(-2, 1, 1))
print(nejvetsi3(-2, 8, 8))
print(nejvetsi3(-5, -5, -5))


# 3b) Funkce pojmenovaná Nejvetsi, která ze seznamu čísel nalezne to největší
def nejvetsiList(seznam):
  storage = 0
  for num in seznam:
    if num > storage:
      storage = num
  return storage

#[x]
seznam2 = [1, -555, 3, 4, 5, 60, 90, 100, -2, -4, 888, 0, 78797879794]
print(nejvetsiList(seznam2))

#4) Funkce NejdelsiString, která pro 2 zadané textové řetězce vrátí ten nejdelší string
def nejdelsiString(text1, text2):
  if len(text1) > len(text2):
    return text1
  elif len(text1) < len(text2):
    return text2
  elif len(text1) == len(text2):
    return "!! Both strings are same lenght: %s" % text1
  else:
    return "You broke the rules, function is weak! :'("

#[x]
print(nejdelsiString("HahaJedna", "sdsds"))
print(nejdelsiString("Dvadva", "HahaJedna"))
print(nejdelsiString("Dvadva", "Dvadva"))
print(nejdelsiString("adasdasdasdasdasd", "pokopaketeplplelplpl"))
print(nejdelsiString("dadaddada dadadada", "Dvadasdasdasddva"))
print(nejdelsiString("dadaddada Lorem, ipsum dolor sit amet consectetur adipisicing elit. Numquam necessitatibus enim laboriosam error consequatur. Ducimus aspernatur totam obcaecati! Facilis, doloribus!", "Dvadasdasdasddva"))
print(nejdelsiString("dadaddada dasdas ahoj ahoj ahoj", "Dvadasdasdasddva"))
print(nejdelsiString("dadaddada dadadada", "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Numquam necessitatibus enim laboriosam error consequatur. Ducimus aspernatur totam obcaecati! Facilis, doloribus!"))

# 5) Funkce SpojStringy, která vrátí nový string vytvořený spojením stringů zadaných seznamem. Jednotlivé stringy jsou spojeny definovaným pojítkem PRIDAT POJITKO
def spojStringy(seznam, pojitko):
  uloziste = ""
  for string in seznam:
    if type(string) == str:
      uloziste = uloziste + pojitko + string
  return uloziste

#[ ]
seznam1 = ["asdasd", "asdassa", "asdasd", "ahoj", 2, "ahpojkk", 4546, 55.5, "string"]
print(spojStringy(seznam1, ", "))

# 6) Funkce UdelejSlovnik, která pro zadaný seznam slov vrátí seznam typů
def udelejSlovnik(seznam):
  storage = []
  for x in seznam:
    word = x.lower()
    if word not in storage:
     storage.append(word)
  return print(storage)

#[ ]
seznam = ["já", "ty", "já", "ty", "my", "oni", "Oni", "já", "Já", "jÁ", "JÁ", "ON", "OnA", "ona"]
udelejSlovnik(seznam)


# 7) Funkce PocetSlabik, která se pokusí odhadnout počet slabik ve slově
# Vyhledá slabikotvorné hlásky ve slově, celkový počet se pak dělí s délkou slova. Pokud je vypočítaný index hustoty slabikotvorných hlásek nižší než 2.5, odečítáme slabiku, pokud je index vyšší nebo roven 3.5 přičítáme počet slabik. 
def pocetSlabik(words):
  find = ["a", "á", "e", "é", "i", "í", "o", "u", "ú", "ů", "l", "r", "y", "ě"]
  stor = 0
  for word in words:
    stor = 0
    for f in find:
      loops = 0
      while loops < len(word):
        loops += 1
        if f in word[(loops - 1)].lower():
          stor += 1
    while (len(word)/stor) < 2.5:
      stor -= 1 
    while (len(word)/stor) >= 3.5:
      stor += 1
    print(word + " " + str(stor) + " " + str(len(word) / stor))

#[ ] "Záludná" slova to většinou nezvládne viz popokatepetl
pocetSlabik(["válka", "pálka", "vlk", "hltat", "prskavka", "hlasivky", "nejhlučnější", "auto", "ucho", "roucho", "louny", "koprovka", "roudná", "ropa", "ryzec", "zrzeček", "rasputin", "nejvzácnější", "popokatepetl", "ropuška", "rozdám", "koleno", "zaskočí"])

#8) Funkce JeStringPalindrom, kteřá vrací True/False, pokud je zadaný string palindrom
def JeStringPalindrom(word):
  wordOrig = word.lower()
  wordReversed = wordOrig[::-1]
  if wordOrig == wordReversed:
    return True
  else:
    return False

print(JeStringPalindrom("pes"))
print(JeStringPalindrom("radar"))
print(JeStringPalindrom("oko"))
print(JeStringPalindrom("robot"))
print(JeStringPalindrom("pepe"))
print(JeStringPalindrom("kajak"))
print(JeStringPalindrom("Anna"))

#9) Funkce JenSude, která pro daný seznam čísel vrátí jen ta sudá

def JenSude(cislo): 
  vypocet = cislo % 2
  if vypocet == 1:
    return False  
  else:
    return True

print(JenSude(2))
print(JenSude(11))
print(JenSude(8))
print(JenSude(222))
print(JenSude(9086))


#10) Funkce MakeBiGrams, která pro seznam tokenů vytvoří jejich bi-gramy spojené "-->"
def makeBiGrams(stringList):
  loop = 0
  for item in stringList:
    loop += 1
    if loop > 1:
      vysledek = storage + "-->" + item
      print(vysledek)
    storage = item

makeBiGrams(["Pes", "je", "přítel", "člověka", "říká", "se", "často", "mezi", "lidmi", "ale", "už", "tolik", "ne", "mezi", "zvířaty"])

#11) Funkce MakeBiGramLists, která pro seznam tokenů vytvoří jejich bi-gramy uložené v seznamech
def MakeBiGramLists (stringList):
  loop = 0
  seznamTemp = []
  seznam = []
  for item in stringList:
    loop += 1
    if loop > 1:
      seznamTemp = []
      seznamTemp.extend([storage, item])
      seznam.append(seznamTemp)
    storage = item
  print(seznam)

MakeBiGramLists(["Pes", "je", "přítel", "člověka", "říká", "se", "často", "mezi", "lidmi", "ale", "už", "tolik", "ne", "mezi", "zvířaty"])

#12) Funkce MakeNGrams, která pro zadaný seznam tokenů, počet N  a lepidlo vytvoří jejich n-gramy
def makeNGrams(stringList, N, pojitko):
  nGrams = N
  startingPoint = 0
  dispersion = N-(N-1)
  output = ""
  loop = 0
  for item in stringList:
    listFin = stringList[startingPoint:nGrams]
    nGrams += dispersion
    startingPoint += dispersion
    if len(listFin) == N:
      for item in listFin:
        loop += 1
        if loop < N:
          output += item + pojitko
        else:
          output += item
      loop = 0
      print(output)
      output = ""



makeNGrams(["Pes", "je", "přítel", "člověka", "říká", "se", "často", "mezi", "lidmi", "ale", "už", "tolik", "ne", "mezi", "zvířaty"], 5, "-->")


#13) Funkce GetTokenInfo, která vrátí dictionare obsahující informace o zadaném tokenu: délka, odhadnutý počet slabik a zda je palindrom. 


def GetTokenInfo(word):
  def JeStringPalindrom(word):
    wordOrig = word.lower()
    wordReversed = wordOrig[::-1]
    if wordOrig == wordReversed:
      return True
    else:
      return False
  
  def pocetSlabik(words):
    find = ["a", "á", "e", "é", "i", "í", "o", "u", "ú", "ů", "l", "r", "y", "ě"]
    stor = 0
    for word in words:
      stor = 0
      for f in find:
        loops = 0
        while loops < len(word):
          loops += 1
          if f in word[(loops - 1)].lower():
            stor += 1
      while (len(word)/stor) < 2.5:
        stor -= 1
      while (len(word)/stor) >= 3.5:
        stor += 1
      return str(stor)

  dictionary = {}
  dictionary["Délka"] = len(word)
  dictionary["Palindrom"] = JeStringPalindrom(word)
  dictionary["Počet slabik"] = pocetSlabik([word])
  return print(dictionary)

GetTokenInfo("Pes")
GetTokenInfo("Radar")
GetTokenInfo("Žemle")
GetTokenInfo("Louno")

#14) Vytvořte vlastní funkci MujStringCompare(a, b), která po jednotlivých znacích otestuje, zda jsou dva textové řetězce stejné. Pokud jsou stejné, funkce vrací True, jinak False
def MujStringCompare(a, b):
  a_compare = []
  b_compare = []
  index_loop = 0
  for i in a:
    a_compare.append(i)
  for i in b:
    b_compare.append(i)
  while a_compare[index_loop] == b_compare[index_loop]:
    print(a_compare[index_loop] + " " + b_compare[index_loop])
    index_loop += 1
    if index_loop == len(a_compare) and len(b_compare):
      return True
  else:
    return False
    

MujStringCompare("lukašenko", "bělorusko")
MujStringCompare("COVID", "COVID")
MujStringCompare("LOPATA", "LOPATKA")


#15) Napište jednoduchý program pro sčítání, který postupně sčítá zadaná čísla a ukazuje mezivýsledek. Uživatel pomocí raw_input vždy zadá jedno číslo, program jej sečte s předchozím výsledkem (pozn.: velmi praktická věc):

def counter():
  storage = 0
  x = True
  while x == True:
    numberRequest = int(input("zadejte číslo: "))
    storage += numberRequest
    message = "Mezisoučet: " + str(storage)
    print(message)

  # counter()


#16) Vytvořte jednoduchou hru: počítač si bude "myslet číslo" a my jej musíme pomocí raw_input uhádnout. Počítač nám napovídá "mé číslo je větší/menší" a "těsně", pokud jsme se minuli o 1. Počet pokusů je počítán a vypsán na konci.

def gameGuess(difficulty):
  from random import randrange
  inputNumber = 0
  loop = 0
  computerNumber = int(randrange(difficulty))
  while inputNumber != computerNumber:
    loop += 1
    inputNumber = int(input("Napiš číslo: "))
    if (inputNumber + 1 == computerNumber) or (inputNumber - 1 == computerNumber):
      print("You almost got me!")
    elif inputNumber > computerNumber:
      print("My number is lower")
    elif inputNumber < computerNumber:
      print("My number is higher")
    else:
      print("You won! " + "You guessed: " + str(loop) + " times")

gameGuess(1000)



#
