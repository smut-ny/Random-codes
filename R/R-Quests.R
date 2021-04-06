## DEPENDENCE
install.packages("stringi")
install.packages("stringr")
source("https://raw.githubusercontent.com/oltkkol/vmod/master/simplest_text.R")


##QUEST 1
#Načtěme do R knihu Švejk a zjistěme, jakou má průměrnou délku slov.

KlimaRaw <- GetFileContent("C:/Users/Tristo/Desktop/klima.txt")
KlimaTok <- TokenizeText(KlimaRaw)
KlimaNchar <- nchar(KlimaTok)
mean(KlimaNchar) #4.666762


##QUEST 2
#Jaká je průměrná délka slov typů („slovníku“)?

KlimaTypes <- unique(KlimaTok)
KlimaTypesNchar <- nchar(KlimaTypes)
mean(KlimaTypesNchar) #6.960354

##QUEST 3
#Jak se mění průměrná délka slov, když text roste?

mean(KlimaNchar[1:10]) -> growth1
mean(KlimaNchar[1:100]) -> growth2
mean(KlimaNchar[1:1000]) -> growth3
mean(KlimaNchar[1:10000]) -> growth4
mean(KlimaNchar) -> growthall


c(growth1, growth2, growth3, growth4, growthall) -> growthY
c(10, 100, 1000, 10000, length(KlimaNchar)) -> growthX

plot(growthX, growthY)


##FOR



tokeny <- TokenizeText(KlimaRaw)


c() -> ulozistePrumeru
for (mojePostupnaDelka in 1:90000){
  tokeny[1:mojePostupnaDelka] -> aktualniVyrezTokenu
  nchar(aktualniVyrezTokenu) -> delkyVyrezuTokenu
  mean(delkyVyrezuTokenu) -> prumer
  append(ulozistePrumeru, prumer) -> ulozistePrumeru
}

plot(1:90000, ulozistePrumeru)


##4

install.packages("stringi")
install.packages("stringr")
source("https://raw.githubusercontent.com/oltkkol/vmod/master/simplest_text.R")


##QUEST 1
#Načtěme do R knihu Švejk a zjistěme, jakou má průměrnou délku slov.

plainTExt <- GetFileContent("C:/Users/Tristo/Desktop/klima.txt")

tokeny <- TokenizeText(plainTExt)

c() -> ulozistePrumeru

2000 -> limitPoctuTokenu

for (mojePostupnaDelka in 1:limitPoctuTokenu){
  tokeny[1:mojePostupnaDelka] -> aktualniVyrezTokenu
  nchar(aktualniVyrezTokenu)  -> delkyZVyrezuTokenu
  
  mean(delkyZVyrezuTokenu) -> prumer
  
  append(ulozistePrumeru, prumer) -> ulozistePrumeru
}

plot( 1:limitPoctuTokenu, ulozistePrumeru )



#################QUEST 2

plainTExt <- GetFileContent("C:/Users/Tristo/Desktop/klima.txt")

tokeny <- TokenizeText(plainTExt)

c() -> ulozistePrumeru

2000 -> limitPoctuTokenu

for (mojePostupnaDelka in 1:limitPoctuTokenu){
  tokeny[1:mojePostupnaDelka] -> aktualniVyrezTokenu

  append(ulozistePrumeru, ttr) -> ulozistePrumeru
}

plot( 1:limitPoctuTokenu, ulozistePrumeru)



#################QUEST 3


english <- GetFileContent("C:/Users/Tristo/Desktop/Matlach/jazyky/EN1.txt")
afr <- GetFileContent("C:/Users/Tristo/Desktop/Matlach/jazyky/afr.txt")
gr <- GetFileContent("C:/Users/Tristo/Desktop/Matlach/jazyky/gr1.txt")


quest3 <- function(x, y) {
  list <- c()
  tokenized <- TokenizeText(x)
  nchared <- nchar(tokenized)
  limit <- y
  
  for (i in 1:limit) {
    tokenized[1:i] -> tokenized_cut
    nchar(tokenized_cut)  -> tokenized_cut_nchar
    mean(tokenized_cut_nchar) -> meanNumber
    append(list, meanNumber) -> list
  }
  
  list
  
}

offsetNum <- 5000



englishPlot <- quest3(english, offsetNum)
afrPlot <- quest3(afr, offsetNum)
grPlot <- quest3(gr, offsetNum)

hist(englishPlot)



listx <- c(1:offsetNum)
plot(listx, englishPlot, type="o", col="blue", pch="o", lty=1, ylim=c(2.5,8.5))

points(listx, afrPlot, col="red", pch="*")
lines(listx, afrPlot, col="red",lty=2)

points(listx, grPlot, col="dark red",pch="+")
lines(listx, grPlot, col="dark red", lty=3)



#######Stochastické modelování

seznamNamerenychPrumeru <- c()

#SLOVA
for (i in 1:1000) {
  klimaSample <- sample(KlimaTok, replace=TRUE)
  namereneDelkyTokenu <- nchar(klimaSample)
  zmerenyPrumer <- mean(namereneDelkyTokenu)
  seznamNamerenychPrumeru <- append(seznamNamerenychPrumeru, zmerenyPrumer)
}

##TYPE
for (i in 1:1000) {
  klimaSample <- sample(KlimaTypes, replace=TRUE)
  namereneDelkyTokenu <- nchar(klimaSample)
  zmerenyPrumer <- mean(namereneDelkyTokenu)
  seznamNamerenychPrumeru <- append(seznamNamerenychPrumeru, zmerenyPrumer)
}


length(seznamNamerenychPrumeru)
hist(seznamNamerenychPrumeru, breaks = 100)
quantile(seznamNamerenychPrumeru, probs=c(0.025, 0.975))


#QUEST: BOOTSTRAP (asi špatně, malý rozptyld  )

english <- GetFileContent("C:/Users/Tristo/Desktop/Matlach/jazyky/EN1.txt")
gr <- GetFileContent("C:/Users/Tristo/Desktop/Matlach/jazyky/ge.txt")
it <- GetFileContent("C:/Users/Tristo/Desktop/Matlach/jazyky/it.txt")
en <- GetFileContent("C:/Users/Tristo/Desktop/Matlach/jazyky/EN1.txt")
en2 <- GetFileContent("C:/Users/Tristo/Desktop/Matlach/jazyky/EN2.txt")

bootstrap <- function(fileRaw){
  maxLoop <- 1000
  seznamNamerenychPrumeru <- c()
  fileTokenized <- TokenizeText(fileRaw)
  fileTokenized <- fileTokenized[1:1000]
  for (i in 1:maxLoop) {
    fileSample <- sample(fileTokenized, replace=TRUE)
    namereneDelkyTokenu <- nchar(fileSample)
    zmerenyPrumer <- mean(namereneDelkyTokenu)
    seznamNamerenychPrumeru <- append(seznamNamerenychPrumeru, zmerenyPrumer)
  }
  return(seznamNamerenychPrumeru)
}

grStrap <- bootstrap(gr)
hist(grStrap, breaks = 100)
quantile(grStrap, probs=c(0.025, 0.975))

itStrap <- bootstrap(it)
hist(itStrap, breaks = 100, add=TRUE, col="green")
quantile(itStrap, probs=c(0.025, 0.975))

enStrap1000 <- bootstrap(en)
hist(enStrap1000, breaks = 100)
quantile(enStrap1000, probs=c(0.025, 0.975))

en2Strap1000 <- bootstrap(en2)
hist(en2Strap1000, breaks = 100, add=TRUE, col="green")
quantile(en2Strap1000, probs=c(0.025, 0.975))

###Quest COMPARE two langs

compareBootstrap <- function(file1, file2){
  maxLoop <- 10000
  seznamNamerenychPrumeru <- c()
  fileTokenized1 <- TokenizeText(file1)
  fileTokenized1 <- fileTokenized1[1:1000]
  fileTokenized2 <- TokenizeText(file2)
  fileTokenized2 <- fileTokenized2[1:1000]
  
  for (i in 1:maxLoop) {
    fileSample1 <- sample(fileTokenized1, replace=TRUE)
    fileSample2 <- sample(fileTokenized2, replace=TRUE)
    namereneDelkyTokenu1 <- nchar(fileSample1)
    namereneDelkyTokenu2 <- nchar(fileSample2)
    zmerenyPrumer1 <- mean(namereneDelkyTokenu1)
    zmerenyPrumer2 <- mean(namereneDelkyTokenu2)
    rozdil <- zmerenyPrumer1-zmerenyPrumer2
    seznamNamerenychPrumeru <- append(seznamNamerenychPrumeru, rozdil)
  }
  return(seznamNamerenychPrumeru)
}

compare <- compareBootstrap(en, en1)
quantile(compare, probs=c(0.025, 0.975))

hist(compare, breaks = 100)


##9. 11. 2020
pismena <- c("A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
vysledek <- c()

for (i in 1:100000){
  pismenaRandom <- sample(pismena, 3)
  pismenaTri <- paste(pismenaRandom, collapse="")
  vysledek <- append(vysledek, pismenaTri)
  
}
vysledek

#LEVACI

vagon <- c(rep("pravak", 83), rep("levak", 9))
vysledek <- c()
progress <- 0


for (i in 1:10000){
  progress <- progress + 1
  kabinka <- sample(vagon, 5, replace = FALSE)
  
  if (kabinka == "levak"){
    pocetLevaku <- sum(kabinka == "levak")
    vysledek <- append(vysledek, pocetLevaku)
  }
  else{
    vysledek <- append(vysledek, 0)
  }
  
  cat(progress)
  cat("\n")
}
quantile(vysledek, probs=c(0.025, 0.975))
table(vysledek)
hist(vysledek)

#Srovnat autory na základě velikosti slovníku
#1. využívá italština odlišnou délku slov než němčina, angličtina.
#2. Jeden výzkumník tvrdí, že velikost slovníku dokáže bez problému odlišit dva autory.
#Ukažte na libovolné dvojici autorů reprezentované 1 knihou (seřiznutou na stejnou délku), zda to platí.
#3. Je v češtině "y" používáno více než "i"? TokenizeText(plainText, "[yi]", regexlsMask=TRUE)

#1.
rawText1 <- GetFileContent("assets/jazyky/it.txt")
rawText2 <- GetFileContent("assets/jazyky/gr1.txt")
rawText3 <- GetFileContent("assets/jazyky/en1.txt")

#2.
viewegh1 <- GetFileContent("assets/knihy/vybijena.txt")
viewegh2 <- GetFileContent("assets/knihy/vychova-divek.txt")
urban1 <- GetFileContent("assets/knihy/Lord-Mord.txt")
urban2 <- GetFileContent("assets/knihy/hastrman.txt")

velikostSlovniku <- function(text, loop) {
  result <- 0
  textTokenize <- TokenizeText(text)
  textsample <- sample(textTokenize, loop, replace=TRUE)
  textnchar <- unique(textsample)
  result <- length(textnchar)
  return(result)
}

velikostSlovniku(viewegh1, 10000)
velikostSlovniku(viewegh2, 10000)
velikostSlovniku(urban1, 10000)
velikostSlovniku(urban2, 10000)

#3.

textRaw <- "Seznam Zprávy zjistily, že organizaci ANO v Brně, kterou poškodila korupční kauza Stoka, má restartovat poslanec Karel Rais. Jeho pozici posiluje fakt, že patří k lidem blízkým šéfovi poslanců Jaroslavu Faltýnkovi.
Článek
Málokdy se ve strukturách ANO odehrává něco politicky dynamického. Většinou se děje především to, co si poručí předseda hnutí a premiér Andrej Babiš.
Pozornost si tudíž zaslouží situace, když se ve voličsky důležitém regionu začíná de facto na zelené louce opět parcelovat vliv. A o to víc, je-li u takového procesu poslanec blízký druhému nejdůležitějšímu činovníkovi ANO Jaroslavu Faltýnkovi.
"

textYI <- TokenizeText(textRaw, "[yi]", regexIsMask=TRUE)
result <- table(textYI)

#chybí bootstrap!


#Quest jednotlivé grafémy italštiny BOXPLOT
## DEPENDENCE
install.packages("stringi")
install.packages("stringr")
source("https://raw.githubusercontent.com/oltkkol/vmod/master/simplest_text.R")

itatext <- GetFileContent("assets/jazyky/it.txt")
textTokenized <- TokenizeText(itatext)
textSampled <- sample(itatext, replace = T)
textLetters <- TokenizeText(textSampled, "[abcdefgahijklmnopqrstuvwxyz]", regexIsMask=TRUE)
itatextLetters <- table(itatextLetters)