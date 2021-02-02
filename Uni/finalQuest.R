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
  tableAppender <- c()
  loopNumber <- 0

  #FUNKCE
  #1. počet typů a tokenů
  getTokensAndTypes <- function (text) {
    token <- length(tokenizedText)
    type <- length(unique(tokenizedText))
    
    tableAppender <- append(tableAppender, c(token, type))  
  }
  
  #2. průměrná délka slov
  getMeanWord<- function(text){
    meanWord <- mean(nchar(text))
    
    tableAppender <- append(tableAppender, meanWord)  
  }
  
  #3. entropie slov
  getEntropy <- function(text){
    tokenTable <- length(tokenizedText)
    
    entropy <- "ENTROPY"
    tableAppender <- append(tableAppender, entropy)
  }
  
  #4. udpipe quests
  getUdpipeInfo <- function(text){
    anotace <- udpipe_annotate(modelUdpipe, x = text)
    tabulkaAnotace <- as.data.frame(anotace)
 
    
    #4.1. Mean sentence
    getMeanSentence <- function(anotatedTable){
      sentenceTable <- table(anotatedTable$sentence_id)
      sentenceListNum <- c()
      for (i in sentenceTable){
        sentenceListNum <- append(i, sentenceListNum)
      }
      meanSentence <- mean(sentenceListNum)
      
      tableAppender <- append(tableAppender, meanSentence)
      
    }
    
    #4.2.Number of Verbs 
    getVerbNum <- function (anotatedTable){
      POS <- tabulkaAnotace$upos
      getVerbs <- length(which(POS == "VERB"))
      getNouns <- grepl("N...2.*", tabulkaAnotace$xpos)%>%
        which()%>%
        length()
      
      tableAppender <- append(tableAppender, c(getVerbs, getNouns))
      
    }
    
    getVerbNum(tabulkaAnotace)
    getMeanSentence(tabulkaAnotace)
  }
  
  #Loop přes všechny texty a iniciace funkcí
  for (text in list) {
    loopNumber <- loopNumber + 1
    tokenizedText <- TokenizeText(text)
    
    
    cat("\n \n")
    cat("Working on: ")
    cat(names(list[loopNumber]))
    
    cat("getTokensAndTypes function \n")
    getTokensAndTypes(tokenizedText)
    cat("getMeanWord function \n")
    getMeanWord(tokenizedText)
    cat("getEntropy function \n")
    getEntropy(tokenizedText)
    cat("getUdpipeInfo function \n")
    getUdpipeInfo(text)
    
  }
  
  return(tableAppender)
  
}


getTextInfo(qfin_loadDirectory)



tableTest <- data.frame()
##Knihy v řádcích
tableTest <- rbind(tableTest, "Jmeno")
