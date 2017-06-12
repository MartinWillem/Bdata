setwd("F:\\school\\jaar2\\periode 4\\BDATA-project\\full_file\\")
setwd("/media/jasper/J_O BIN2B/school/jaar2/periode 4/BDATA-project/full_file/")
dir()

install.packages("VIM")
library(VIM)

#Genes_relation vervangen
data <- read.csv("Full_File_data.txt", header = F)
head(data)
colnames(data)
summary(data)
dim(data)

for (x in colnames(data)){
  data[,x][data[,x]=="?"] <- NA
  data[,x][data[,x]=="Unknown"] <- NA
  print(x)
  if (sum(is.na(data[,x]))==862) {
    data[,x] <- NULL
  }
}


head(data)
dim(data)

data2 <- kNN(data, variable = colnames(data), k = 3)
warnings()

dim(data2)
summary(data2)
head(data2)
sub_data <- subset(data2, select = V1:V2960)
head(sub_data)
dim(sub_data)
colnames(sub_data)
write.csv(sub_data, "k-nn_Full_File_data.txt", row.names = F)
