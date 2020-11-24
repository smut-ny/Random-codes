#Dependencies
install.packages("stringi")
install.packages("stringr")
source("https://raw.githubusercontent.com/oltkkol/vmod/master/simplest_text.R")






#PROGRAM 1
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

progress_bar <- 0

for (i in 1:100){
    #Sampling tokenized text file
    textSampled <- sample(textTokenized, replace=TRUE)

    #Appending characters
    vocList[["a"]] <- append(vocList[["a"]], sum(str_count(textSampled, "a")))
    vocList[["b"]] <- append(vocList[["b"]], sum(str_count(textSampled, "b")))
    vocList[["c"]] <- append(vocList[["c"]], sum(str_count(textSampled, "c")))
    vocList[["d"]] <- append(vocList[["d"]], sum(str_count(textSampled, "d")))
    vocList[["e"]] <- append(vocList[["e"]], sum(str_count(textSampled, "e")))
    vocList[["f"]] <- append(vocList[["f"]], sum(str_count(textSampled, "f")))
    vocList[["g"]] <- append(vocList[["g"]], sum(str_count(textSampled, "g")))
    vocList[["h"]] <- append(vocList[["h"]], sum(str_count(textSampled, "h")))
    vocList[["i"]] <- append(vocList[["i"]], sum(str_count(textSampled, "i")))
    vocList[["j"]] <- append(vocList[["j"]], sum(str_count(textSampled, "j")))
    vocList[["k"]] <- append(vocList[["k"]], sum(str_count(textSampled, "k")))
    vocList[["l"]] <- append(vocList[["l"]], sum(str_count(textSampled, "l")))
    vocList[["m"]] <- append(vocList[["m"]], sum(str_count(textSampled, "m")))
    vocList[["n"]] <- append(vocList[["n"]], sum(str_count(textSampled, "n")))
    vocList[["o"]] <- append(vocList[["o"]], sum(str_count(textSampled, "o")))
    vocList[["p"]] <- append(vocList[["p"]], sum(str_count(textSampled, "p")))
    vocList[["q"]] <- append(vocList[["q"]], sum(str_count(textSampled, "q")))
    vocList[["r"]] <- append(vocList[["r"]], sum(str_count(textSampled, "r")))
    vocList[["s"]] <- append(vocList[["s"]], sum(str_count(textSampled, "s")))
    vocList[["t"]] <- append(vocList[["t"]], sum(str_count(textSampled, "t")))
    vocList[["u"]] <- append(vocList[["u"]], sum(str_count(textSampled, "u")))
    vocList[["v"]] <- append(vocList[["v"]], sum(str_count(textSampled, "v")))
    vocList[["w"]] <- append(vocList[["w"]], sum(str_count(textSampled, "w")))
    vocList[["x"]] <- append(vocList[["x"]], sum(str_count(textSampled, "x")))
    vocList[["y"]] <- append(vocList[["y"]], sum(str_count(textSampled, "y")))
    vocList[["z"]] <- append(vocList[["z"]], sum(str_count(textSampled, "z")))


    progress_bar <- progress_bar + 1
    cat(progress_bar)
    cat("\n")
}

boxplot(vocList)


#PROGRAM 2
#Loading and cleaning text file
rawText <- GetFileContent("assets/jazyky/it.txt")
textABC <- TokenizeText(textSampled, regexPattern = "[abcdefghijklmnopqrstuvwxyz]", regexIsMask = T)
progress_bar <- 0

for (i in 1:10000){
    textSampled <- sample(textABC, replace=TRUE)
    textSampledTable <- table(textSampled)
    textSampledList <- split(textSampledTable, seq(rownames(textSampledTable)))
    
    if (i == 1){
        finalList <- textSampledList
    }
    else{
        finalList <- Map(c, finalList, textSampledList)
    }
    
    progress_bar <- progress_bar + 1
    cat(progress_bar)
    cat("\n")
}

boxplot(finalList)

   

#MESS
TextTokenizedAlt <- TokenizeText(rawText, regexPattern = "[abcdefghijklmnopqrstuvwxyz]", regexIsMask = T)
TextToSampled <- sample(TextTokenizedAlt, replace = T)
TextTokenizedTable <- table(TextToSampled)
TextTokenizedTable
Map(c, list1, list2)
abc <- c("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")


