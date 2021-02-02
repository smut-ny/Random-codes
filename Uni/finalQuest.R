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
  loopNumber <- 0
  textInfoTable <- data.frame()

  #Loop přes všechny texty a iniciace funkcí
  for (text in list) {
    loopNumber <- loopNumber + 1
    tokenizedText <- TokenizeText(text)
    textName <- names(list[loopNumber])

    cat("\n \n")
    cat("Working on: ")
    cat(textName)

    #FUNKCE
    #1. počet typů a tokenů
    token <- length(tokenizedText)
    type <- length(unique(tokenizedText))

    #2. průměrná délka slov
    meanWord <- mean(nchar(tokenizedText))
    
    #3. entropie slov
    p <- table(token) / type
    getEntropy <- sum(p * log(p))
	

    #4. udpipe quests
      anotace <- udpipe_annotate(modelUdpipe, x = text)
      tabulkaAnotace <- as.data.frame(anotace)

    #4.1. Mean sentence
      sentenceTable <- table(tabulkaAnotace$sentence_id)
      sentenceListNum <- c()
      for (i in sentenceTable){
        sentenceListNum <- append(i, sentenceListNum)
      }
      meanSentence <- mean(sentenceListNum)
    
    #4.2.Number of Verbs 
      POS <- tabulkaAnotace$upos
      getVerbs <- length(which(POS == "VERB"))
      getNouns <- grepl("N...2.*", tabulkaAnotace$xpos)%>%
        which()%>%
        length()

      textInfoTable <- rbind(textInfoTable, c(token, type, meanSentence, getEntropy, getVerbs, getNouns))
   }
  colnames(textInfoTable) <- c("token", "types", "mean sentence", "entropy", "verbs", "nouns")
  textInfoTable
}


getTextInfo(qfin_loadDirectory)



tableTest <- data.frame()
##Knihy v řádcích
tableTest <- rbind(tableTest, "Jmeno")
