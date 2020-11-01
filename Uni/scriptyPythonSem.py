words = ["válka", "pálka", "vlk", "hltat", "prskavka", "hlasivky", "nejhlučnější", "auto", "ucho", "roucho", "louny", "koprovka", "roudná", "ropa", "ryzec", "zrzeček", "rasputin", "nejvzácnější", "popokatepetl", "ropuška", "rozdám", "koleno", "zaskočí"]
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