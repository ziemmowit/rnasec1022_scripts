library(DESeq2)
library(airway)
library(tidyverse)

setwd("~/NoSync/analiza/mapped")
counts_data <- read.csv('group1.csv')

col_data <- read.csv("group1.coldata.csv")
dds <- DESeqDataSetFromMatrix(countData = counts_data, colData = col_data, design = ~ condition)
dds <- DESeq(dds)
res <-results(dds)
write.table(res, file = "res.csv", sep = ',', col.names = T, row.names = T, quote = F)