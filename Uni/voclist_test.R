#Dependencies
install.packages("stringi")
install.packages("stringr")
source("https://raw.githubusercontent.com/oltkkol/vmod/master/simplest_text.R")

#Loading and cleaning text file
rawText <- GetFileContent("assets/jazyky/it.txt")
textTokenized <- TokenizeText(rawText)

#Main storage (list) that represents final object
vocList <- list()

#Mapping characters in a list
vocList[["a"]] <- c()
vocList[["b"]] <- c()
vocList[["c"]] <- c()
vocList[["d"]] <- c()
vocList[["e"]] <- c()
vocList[["f"]] <- c()
vocList[["g"]] <- c()
vocList[["h"]] <- c()
vocList[["i"]] <- c()
vocList[["j"]] <- c()
vocList[["k"]] <- c()
vocList[["l"]] <- c()
vocList[["m"]] <- c()
vocList[["n"]] <- c()
vocList[["o"]] <- c()
vocList[["p"]] <- c()
vocList[["q"]] <- c()
vocList[["r"]] <- c()
vocList[["s"]] <- c()
vocList[["t"]] <- c()
vocList[["u"]] <- c()
vocList[["v"]] <- c()
vocList[["w"]] <- c()
vocList[["x"]] <- c()
vocList[["y"]] <- c()
vocList[["z"]] <- c()

#Looping: sample whole text and append characters into a mapped list

for (i in 1:100){
    #Sampling tokenized text file
    textSampled <- sample(textTokenized, replace=TRUE)
    
    #Dividing characters from sampled text into table
    textCharacters <- TokenizeText(textSampled, "[abcdefgahijklmnopqrstuvwxyz]", regexIsMask=TRUE)
    textCharacters <- table(textCharacters)
    
    #Appending characters into mapped list
    if (textCharacters[["a"]] == TRUE) {
       
    }
    vocList[["a"]] <- append(textCharacters[["a"]], vocList[["a"]])
    vocList[["b"]] <- append(textCharacters[["b"]], vocList[["b"]])
    vocList[["c"]] <- append(textCharacters[["c"]], vocList[["c"]])
    vocList[["d"]] <- append(textCharacters[["d"]], vocList[["d"]])
    vocList[["e"]] <- append(textCharacters[["e"]], vocList[["e"]])
    vocList[["f"]] <- append(textCharacters[["f"]], vocList[["f"]])
    vocList[["g"]] <- append(textCharacters[["g"]], vocList[["g"]])
    vocList[["h"]] <- append(textCharacters[["h"]], vocList[["h"]])
    vocList[["i"]] <- append(textCharacters[["i"]], vocList[["i"]])
    vocList[["j"]] <- append(textCharacters[["j"]], vocList[["j"]])
    vocList[["k"]] <- append(textCharacters[["k"]], vocList[["k"]])
    vocList[["l"]] <- append(textCharacters[["l"]], vocList[["l"]])
    vocList[["m"]] <- append(textCharacters[["m"]], vocList[["m"]])
    vocList[["n"]] <- append(textCharacters[["n"]], vocList[["n"]])
    vocList[["o"]] <- append(textCharacters[["o"]], vocList[["o"]])
    vocList[["p"]] <- append(textCharacters[["p"]], vocList[["p"]])
    vocList[["q"]] <- append(textCharacters[["q"]], vocList[["q"]])
    vocList[["r"]] <- append(textCharacters[["r"]], vocList[["r"]])
    vocList[["s"]] <- append(textCharacters[["s"]], vocList[["s"]])
    vocList[["t"]] <- append(textCharacters[["t"]], vocList[["t"]])
    vocList[["u"]] <- append(textCharacters[["u"]], vocList[["u"]])
    vocList[["v"]] <- append(textCharacters[["v"]], vocList[["v"]])
    vocList[["w"]] <- append(textCharacters[["w"]], vocList[["w"]])
    vocList[["q"]] <- append(textCharacters[["q"]], vocList[["q"]])
    vocList[["y"]] <- append(textCharacters[["y"]], vocList[["y"]])
    vocList[["z"]] <- append(textCharacters[["z"]], vocList[["z"]])
}

#Appenduje to prazdnej list.. to nejde protoze to hleda podle indexu