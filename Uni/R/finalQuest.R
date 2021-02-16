#Dependencies
library(tidyverse)
library("stringi")
library("stringr")
library("udpipe")
library("tidyverse")
source("https://raw.githubusercontent.com/oltkkol/vmod/master/simplest_text.R")
qfin_loadDirectory <- GetFilesContentsFromFolder("assets/finalQuestDir")
infoStazeni <- udpipe_download_model(language="czech")
modelUdpipe <- udpipe_load_model(file = infoStazeni$file_model)


getTextInfo <- function(list){
  #Deklarace vars
  loopNumber <- 0
  textInfoTable <- data.frame()


  #Loop skrze všechny texty
  for (text in list) {
    loopNumber <- loopNumber + 1
    tokenizedText <- TokenizeText(text)
    textName <- names(list[loopNumber])

    cat("\n \n Working on: ")
    cat(textName)


    #JEDNOTLIVÉ FUNKCE
    #1. Počet typů a tokenů
    getToken <- length(tokenizedText)
    getType <- length(unique(tokenizedText))

    #2. Průměrná délka slov
    getMeanWord <- mean(nchar(tokenizedText))
    
    #3. Entropie slov
    p <- table(getToken) / getType

    getEntropy <- - sum(p * log(p))
	
    #4. Udpipe questy (model, anotace)
    annotate <- udpipe_annotate(modelUdpipe, x = text)
    tableAnnotated <- as.data.frame(annotate)

    #4.1. Průměrná délka vět
    sentenceTable <- table(tableAnnotated$sentence_id)
    sentenceListNum <- c()
    for (sentence in sentenceTable){sentenceListNum <- append(sentence, sentenceListNum)}

    getMeanSentence <- mean(sentenceListNum)
    
    #4.2. Celkový počet sloves a podstatných jmen ve 2. pádu 
    POS <- tableAnnotated$upos

    getVerbs <- length(which(POS == "VERB"))
    getNouns <- grepl("N...2.*", tableAnnotated$xpos)%>%
      which()%>%
      length()

    #Vložení do tabulky
    textInfoTable <- rbind(textInfoTable, c(getToken, getType, getMeanWord, getMeanSentence, getEntropy, getVerbs, getNouns))
   }

  #Pojmenování řádků a seznamů tabulky
  colnames(textInfoTable) <- c("Počet tokenů", "Počet typů", "Průměrná délka slov", "Průměrná délka vět", "Entropie", "Verbs", "Nouns (2. pád)")
  rownames(textInfoTable) <- names(list)
  
  return(textInfoTable)
}


getTextInfo(qfin_loadDirectory)
