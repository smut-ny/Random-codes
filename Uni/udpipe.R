install.packages("udpipe")
library("udpipe")

infoStazeni <- udpipe_download_model(language="czech")
infoStazeni[["file_model"]]

modelUdpipe <- udpipe_load_model(file = infoStazeni$file_model)

rawText <- GetFileContent("assets/knihy/hastrman-vysek.txt")
anotace <- udpipe_annotate(modelUdpipe, x = rawText)
tabulkaAnotace <- as.data.frame(anotace)

head(tabulkaAnotace)
  head(tabulkaAnotace, 100)
colnames(tabulkaAnotace)
ncol(tabulkaAnotace)
rownames(tabulkaAnotace)
nrow(tabulkaAnotace)

tabulkaAnotace[1, 4]
tabulkaAnotace[c(1,2,3), "lemma"]
tabulkaAnotace[1, ]
tabulkaAnotace[1, "token"]
tabulkaAnotace[, "lemma"]




##QUEST 1
tabulkaAnotace[ , "upos"]    -> slovniDruhy
which( slovniDruhy == "ADJ") -> indexyADJ
which( slovniDruhy == "NOUN") -> indexyNOUN
which( slovniDruhy == "VERB") -> indexyVERB
which( slovniDruhy == "CCONJ") -> indexyCCONJ

tabulkaAnotace[indexyADJ, "lemma"] -> lemmataADJ
tabulkaAnotace[indexyNOUN, "lemma"] -> lemmataNOUN
tabulkaAnotace[indexyVERB, "lemma"] -> lemmataVERB
tabulkaAnotace[indexyCCONJ, "lemma"] -> lemmataCCONJ


sample(lemmataADJ, 1)
sample(lemmataNOUN, 1)
sample(lemmataVERB, 1)
sample(lemmataCCONJ, 1)
sample(lemmataVERB, 1)

randomSentence <- c(
  sample(lemmataADJ, 1),
  sample(lemmataNOUN, 1),
  sample(lemmataVERB, 1),
  sample(lemmataCCONJ, 1),
  sample(lemmataVERB, 1)
)

randomSentence

##Prumerna delka vet
sentenceTable <- table(tabulkaAnotace$sentence_id)
sentenceListNum <- c()
for (i in sentenceTable){
  sentenceListNum <- append(i, sentenceListNum)
}
mean(sentenceListNum)



grepl()
substr()
head(tabulkaAnotace[nrow])


sort(table(lemmata), decreasing = TRUE)


tabulkaAnotace$upos


adjektivum <- nahodneSlovo[adj]

nahodneSlovo

table(tabulkaAnotace$upos)
