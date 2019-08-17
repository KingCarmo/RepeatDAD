#install.packages("rvest")
library(rvest)
library(stringr)
library(htmltab)

##### Gathering Data ######

##### Suits season 2 ######
library(htmltab)

url2 <- "https://en.wikipedia.org/wiki/Suits_(season_2)"

SuitsS2 <- htmltab(doc = url2, which = 3)


rownames(SuitsS2) <- c(1:16)

SuitsS2$`Time slot (EST)` <- NULL
SuitsS2$`Rating(Adults 18â€“49)` <- NULL
SuitsS2$`18-49 Rankon Cable`<- NULL
SuitsS2$`Weekly rank` <- NULL

SuitsS2["season"] <- 2
SuitsS2$season <- as.integer(SuitsS2$season)

SuitsS2["name"] <- "Suits"

colnames(SuitsS2)[1] <- "number_in_series"
SuitsS2$number_in_series<- c(13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28)
SuitsS2$number_in_season <- c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
colnames(SuitsS2)[2] <- "title"
colnames(SuitsS2)[3] <- "original_air_date"
colnames(SuitsS2)[4] <- "viewers"

SuitsS2 <- SuitsS2[,c(6,1,7,2,3,4,5)]

##### Suits season 3 ######
library(htmltab)

url3 <- "https://en.wikipedia.org/wiki/Suits_(season_3)"

SuitsS3 <- htmltab(doc = url3, which = 5)


rownames(SuitsS3) <- c(1:16)

SuitsS3$`Time slot (EST)` <- NULL
SuitsS3$`Rating(Adults 18â€“49)` <- NULL
SuitsS3$`18-49 Rankon Cable`<- NULL
SuitsS3$`Weekly rank` <- NULL

SuitsS3["season"] <- 3
SuitsS3$season <- as.integer(SuitsS3$season)

SuitsS3["name"] <- "Suits"

colnames(SuitsS3)[1] <- "number_in_series"
SuitsS3$number_in_series<- c(29:44)
SuitsS3$number_in_season <- c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
colnames(SuitsS3)[2] <- "title"
colnames(SuitsS3)[3] <- "original_air_date"
colnames(SuitsS3)[4] <- "viewers"

SuitsS3 <- SuitsS3[,c(6,1,7,2,3,4,5)]

##### Suits season 4 ######
library(htmltab)

url4 <- "https://en.wikipedia.org/wiki/Suits_(season_4)"

SuitsS4 <- htmltab(doc = url4, which = 4)


rownames(SuitsS4) <- c(1:16)

SuitsS4$`Time slot (EST)` <- NULL
SuitsS4$`Rating(Adults 18â€“49)` <- NULL
SuitsS4$`18-49 Rankon Cable`<- NULL
SuitsS4$`Weekly rank` <- NULL

SuitsS4["season"] <- 4
SuitsS4$season <- as.integer(SuitsS4$season)

SuitsS4["name"] <- "Suits"

colnames(SuitsS4)[1] <- "number_in_series"
SuitsS4$number_in_series<- c(45:60)
SuitsS4$number_in_season <- c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
colnames(SuitsS4)[2] <- "title"
colnames(SuitsS4)[3] <- "original_air_date"
colnames(SuitsS4)[4] <- "viewers"

SuitsS4 <- SuitsS4[,c(6,1,7,2,3,4,5)]

##### Suits season 5 ######
library(htmltab)

url5 <- "https://en.wikipedia.org/wiki/Suits_(season_5)"

SuitsS5 <- htmltab(doc = url5, which = 3)


rownames(SuitsS5) <- c(1:16)

SuitsS5$`Time slot (EST)` <- NULL
SuitsS5$`Rating(Adults 18â€“49)` <- NULL
SuitsS5$`18-49 Rankon Cable`<- NULL
SuitsS5$`Weekly rank` <- NULL

SuitsS5["season"] <- 5
SuitsS5$season <- as.integer(SuitsS5$season)

SuitsS5["name"] <- "Suits"

colnames(SuitsS5)[1] <- "number_in_series"
SuitsS5$number_in_series<- c(61:76)
SuitsS5$number_in_season <- c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
colnames(SuitsS5)[2] <- "title"
colnames(SuitsS5)[3] <- "original_air_date"
colnames(SuitsS5)[4] <- "viewers"

SuitsS5 <- SuitsS5[,c(6,1,7,2,3,4,5)]

##### Suits season 6 ######
library(htmltab)

url6 <- "https://en.wikipedia.org/wiki/Suits_(season_8)"

SuitsS6 <- htmltab(doc = url6, which = 3)


rownames(SuitsS6) <- c(1:16)

SuitsS6$`DVR(18â€“49)`<- NULL
SuitsS6$`Total(18â€“49)`<- NULL
SuitsS6$`DVR viewers(millions)` <- NULL
SuitsS6$`Rating(18â€“49)` <- NULL
SuitsS6$`Total viewers(millions)`<- NULL

SuitsS6["season"] <- 6
SuitsS6$season <- as.integer(SuitsS6$season)

SuitsS6["name"] <- "Suits"

colnames(SuitsS6)[1] <- "number_in_series"
SuitsS6$number_in_series<- c(77:92)
SuitsS6$number_in_season <- c(1,2,3,4,6,6,7,8,9,10,11,12,13,14,15,16)
colnames(SuitsS6)[2] <- "title"
colnames(SuitsS6)[3] <- "original_air_date"
colnames(SuitsS6)[4] <- "viewers"

SuitsS6 <- SuitsS6[,c(6,1,7,2,3,4,5)]

#install.packages("rvest")
#install.packages("tidyverse")
#install.packages("tidyr")
library(rvest)
library(stringr)
library(tidyverse)
library(tidyr)

############################ Suits ##################################

SuitsS2Rating <- read_html("https://www.imdb.com/list/ls053803763/")

### S2 ###
S2EP1 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[1]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP2 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[2]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()


S2EP3 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[3]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP4 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[4]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP5 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[5]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP6 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[6]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP7 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[7]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP8 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[8]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP9 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[9]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP10 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[10]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP11 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[11]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP12 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[12]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP13 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[13]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP14 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[14]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP15 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[15]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S2EP16 <- SuitsS2Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[16]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

SuitsS3Rating <- read_html("https://www.imdb.com/list/ls053836113/")

### S3 ###
S3EP1 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[1]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP2 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[2]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()


S3EP3 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[3]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP4 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[4]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP5 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[5]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP6 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[6]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP7 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[7]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP8 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[8]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP9 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[9]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP10 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[10]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP11 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[11]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP12 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[12]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP13 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[13]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP14 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[14]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP15 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[15]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S3EP16 <- SuitsS3Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[16]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()


SuitsS4Rating <- read_html("https://www.imdb.com/list/ls070725087/")

### S4 ###
S4EP1 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[1]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP2 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[2]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()


S4EP3 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[3]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP4 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[4]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP5 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[5]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP6 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[6]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP7 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[7]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP8 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[8]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP9 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[9]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP10 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[10]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP11 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[11]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP12 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[12]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP13 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[13]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP14 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[14]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP15 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[15]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S4EP16 <- SuitsS4Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[16]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

SuitsS5Rating <- read_html("https://www.imdb.com/list/ls074591904/")

### S5 ###
S5EP1 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[1]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP2 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[2]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()


S5EP3 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[3]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP4 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[4]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP5 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[5]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP6 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[6]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP7 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[7]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP8 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[8]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP9 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[9]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP10 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[10]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP11 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[11]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP12 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[12]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP13 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[13]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP14 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[14]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP15 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[15]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

S5EP16 <- SuitsS5Rating %>%
  html_nodes(xpath = '//*[@id="main"]/div/div[4]/div[3]/div[16]/div[2]/div[1]/div[1]/span[2]') %>%
  html_text()

SuitsS6Rating <- read_html("https://www.imdb.com/title/tt1632701/episodes?season=8")


### S6 ###
S6EP1 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP2 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP3 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP4 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP5 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP6 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP7 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP8 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[8]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP9 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[9]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP10 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[10]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP11 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[11]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP12 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[12]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP13 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[13]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP14 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[14]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP15 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[15]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S6EP16 <- SuitsS6Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[16]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()


Ratings <- as.data.frame(as.double(cbind(S2EP1, S2EP2, S2EP3, S2EP4, S2EP5, S2EP6, S2EP7, S2EP8, S2EP9, S2EP10, S2EP11, S2EP12, S2EP13, S2EP14, S2EP15, S2EP16,
                                         S3EP1, S3EP2, S3EP3, S3EP4, S3EP5, S3EP6, S3EP7, S3EP8, S3EP9, S3EP10, S3EP11, S3EP12, S3EP13, S3EP14, S3EP15, S3EP16,
                                         S4EP1, S4EP2, S4EP3, S4EP4, S4EP5, S4EP6, S4EP7, S4EP8, S4EP9, S4EP10, S4EP11, S4EP12, S4EP13, S4EP14, S4EP15, S4EP16,
                                         S5EP1, S5EP2, S5EP3, S5EP4, S5EP5, S5EP6, S5EP7, S5EP8, S5EP9, S5EP10, S5EP11, S5EP12, S5EP13, S5EP14, S5EP15, S5EP16,
                                         S6EP1, S6EP2, S6EP3, S6EP4, S6EP5, S6EP6, S6EP7, S6EP8, S6EP9, S6EP10, S6EP11, S6EP12, S6EP13, S6EP14, S6EP15, S6EP16
)))

colnames(Ratings)
names(Ratings)[1] <- "Ratings"

##### Combining Code ######
SuitsFull <- rbind(SuitsS2, SuitsS3, SuitsS4, SuitsS5, SuitsS6)
SuitsFull <- cbind(SuitsFull, Ratings)

SuitsFull$viewers <- as.double(SuitsFull$viewers)
SuitsFull$Ratings <- as.double(SuitsFull$Ratings)

##### Creating Suits CSV Files #####
write.csv((SuitsFull), "Suits_Dataset.csv")

##### NCIS S12 #####
library(htmltab)

url6 <- "https://en.wikipedia.org/wiki/NCIS_(season_12)"

NcisS12 <- htmltab(doc = url6, which = 4)

rownames(NcisS12) <- c(1:24)

NcisS12$`Ratings >> Live >> Rating/share(18â€“49)` <- NULL
NcisS12$`Ratings >> Live+7 >> Rating/share(18â€“49))` <- NULL
NcisS12$`Ratings >> Live rank(viewers) >> Night`<- NULL
NcisS12$`Ratings >> Live rank(viewers) >> Week` <- NULL
NcisS12$`Ratings >> Live+7 >> Viewers(millions)`<- NULL


NcisS12["season"] <- 12
NcisS12$season <- as.integer(NcisS12$season)

NcisS12["name"] <- "Ncis"

NcisS12$number_in_series <- c(259:282)
NcisS12$number_in_season <- c(1:24)
colnames(NcisS12)[1] <- "title"
colnames(NcisS12)[2] <- "original_air_date"
colnames(NcisS12)[3] <- "viewers"
colnames(NcisS12)[6] <- "number_in_series"

NcisS12 <- NcisS12[,c(5,6,7,1,2,3,4)]

##### NCIS S13 #####
library(htmltab)

url7 <- "https://en.wikipedia.org/wiki/NCIS_(season_13)"

NcisS13 <- htmltab(doc = url7, which = 3)


rownames(NcisS13) <- c(1:24)

NcisS13$`Rating/share(18â€“49)` <- NULL
NcisS13$`DVR(18â€“49)` <- NULL
NcisS13$`DVR viewers(millions)`<- NULL
NcisS13$`Total(18â€“49)`<- NULL
NcisS13$`Total viewers(millions)`<- NULL


NcisS13["season"] <- 13
NcisS13$season <- as.integer(NcisS13$season)

NcisS13["name"] <- "Ncis"

NcisS13$number_in_series <- c(283:306)
NcisS13$number_in_season <- c(1:24)
NcisS13 <- NcisS13[,-c(1)]
colnames(NcisS13)[1] <- "title"
colnames(NcisS13)[2] <- "original_air_date"
colnames(NcisS13)[3] <- "viewers"

NcisS13 <- NcisS13[,c(5,6,7,1,2,3,4)]


##### NCIS S14 #####
library(htmltab)

url8 <- "https://en.wikipedia.org/wiki/NCIS_(season_14)"

NcisS14 <- htmltab(doc = url8, which = 3)


rownames(NcisS14) <- c(1:24)

NcisS14$`Rating/share(18â€“49)` <- NULL
NcisS14$`DVR(18â€“49)` <- NULL
NcisS14$`DVR viewers(millions)`<- NULL
NcisS14$`Total(18â€“49)`<- NULL
NcisS14$`Total viewers(millions)`<- NULL


NcisS14["season"] <- 14
NcisS14$season <- as.integer(NcisS14$season)

NcisS14["name"] <- "Ncis"

NcisS14$number_in_series <- c(307:330)
NcisS14$number_in_season <- c(1:24)
NcisS14 <- NcisS14[,-c(1)]
colnames(NcisS14)[1] <- "title"
colnames(NcisS14)[2] <- "original_air_date"
colnames(NcisS14)[3] <- "viewers"

NcisS14 <- NcisS14[,c(5,6,7,1,2,3,4)]

##### NCIS S15 #####
library(htmltab)

url9 <- "https://en.wikipedia.org/wiki/NCIS_(season_15)"

NcisS15 <- htmltab(doc = url9, which = 3)

rownames(NcisS15) <- c(1:24)

NcisS15$`Rating/share(18â€“49)` <- NULL
NcisS15$`DVR(18â€“49)` <- NULL
NcisS15$`DVR viewers(millions)`<- NULL
NcisS15$`Total(18â€“49)`<- NULL
NcisS15$`Total viewers(millions)`<- NULL


NcisS15["season"] <- 15
NcisS15$season <- as.integer(NcisS15$season)

NcisS15["name"] <- "Ncis"

NcisS15$number_in_series <- c(331:354)
NcisS15$number_in_season <- c(1:24)
NcisS15 <- NcisS15[,-c(1)]
colnames(NcisS15)[1] <- "title"
colnames(NcisS15)[2] <- "original_air_date"
colnames(NcisS15)[3] <- "viewers"

NcisS15 <- NcisS15[,c(5,6,7,1,2,3,4)]

##### NCIS S16 #####
library(htmltab)

url10 <- "https://en.wikipedia.org/wiki/NCIS_(season_16)"

NcisS16 <- htmltab(doc = url10, which = 3)

rownames(NcisS16) <- c(1:24)

NcisS16$`Rating/share(18â€“49)` <- NULL
NcisS16$`DVR(18â€“49)` <- NULL
NcisS16$`DVR viewers(millions)`<- NULL
NcisS16$`Total(18â€“49)`<- NULL
NcisS16$`Total viewers(millions)`<- NULL


NcisS16["season"] <- 16
NcisS16$season <- as.integer(NcisS16$season)

NcisS16["name"] <- "Ncis"

NcisS16$number_in_series <- c(355:378)
NcisS16$number_in_season <- c(1:24)
NcisS16 <- NcisS16[,-c(1)]
colnames(NcisS16)[1] <- "title"
colnames(NcisS16)[2] <- "original_air_date"
colnames(NcisS16)[3] <- "viewers"

NcisS16 <- NcisS16[,c(5,6,7,1,2,3,4)]


#install.packages("rvest")
#install.packages("tidyverse")
#install.packages("tidyr")
library(rvest)
library(stringr)
library(tidyverse)
library(tidyr)

############################ NCIS ##################################

NCISS12Rating <- read_html("https://www.imdb.com/title/tt0364845/episodes?season=12")

### S12 ###
S12EP1 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP2 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP3 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP4 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP5 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP6 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP7 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP8 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[8]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP9 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[9]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP10 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[10]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP11 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[11]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP12 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[12]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP13 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[13]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP14 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[14]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP15 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[15]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP16 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[16]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP17 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[17]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP18 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[18]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP19 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[19]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP20 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[20]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP21 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[21]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP22 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[22]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP23 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[23]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S12EP24 <- NCISS12Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[24]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()


NCISS13Rating <- read_html("https://www.imdb.com/title/tt0364845/episodes?season=13")

### S13 ###
S13EP1 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP2 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP3 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP4 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP5 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP6 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP7 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP8 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[8]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP9 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[9]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP10 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[10]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP11 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[11]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP12 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[12]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP13 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[13]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP14 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[14]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP15 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[15]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP16 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[16]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP17 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[17]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP18 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[18]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP19 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[19]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP20 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[20]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP21 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[21]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP22 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[22]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP23 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[23]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S13EP24 <- NCISS13Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[24]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()


NCISS14Rating <- read_html("https://www.imdb.com/title/tt0364845/episodes?season=13")

### S14 ###
S14EP1 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP2 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP3 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP4 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP5 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP6 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP7 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP8 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[8]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP9 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[9]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP10 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[10]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP11 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[11]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP12 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[12]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP13 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[13]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP14 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[14]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP15 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[15]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP16 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[16]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP17 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[17]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP18 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[18]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP19 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[19]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP20 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[20]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP21 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[21]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP22 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[22]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP23 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[23]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S14EP24 <- NCISS14Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[24]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()


NCISS15Rating <- read_html("https://www.imdb.com/title/tt0364845/episodes?season=13")

### S15 ###
S15EP1 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP2 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP3 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP4 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP5 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP6 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP7 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP8 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[8]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP9 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[9]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP10 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[10]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP11 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[11]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP12 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[12]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP13 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[13]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP14 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[14]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP15 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[15]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP16 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[16]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP17 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[17]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP18 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[18]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP19 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[19]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP20 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[20]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP21 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[21]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP22 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[22]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP23 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[23]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S15EP24 <- NCISS15Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[24]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()


NCISS16Rating <- read_html("https://www.imdb.com/title/tt0364845/episodes?season=13")

### S16 ###
S16EP1 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP2 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP3 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP4 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP5 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP6 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP7 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP8 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[8]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP9 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[9]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP10 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[10]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP11 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[11]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP12 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[12]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP13 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[13]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP14 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[14]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP15 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[15]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP16 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[16]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP17 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[17]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP18 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[18]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP19 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[19]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP20 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[20]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP21 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[21]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP22 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[22]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP23 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[23]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S16EP24 <- NCISS16Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[24]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()


Ratings <- as.data.frame(as.double(cbind(S12EP1, S12EP2, S12EP3, S12EP4, S12EP5, S12EP6, S12EP7, S12EP8, S12EP9, S12EP10, S12EP11, S12EP12, S12EP13, S12EP14, S12EP15, S12EP16,S12EP17,S12EP18,S12EP19,S12EP20,S12EP21,S12EP22,S12EP23,S12EP24,
                                         S13EP1, S13EP2, S13EP3, S13EP4, S13EP5, S13EP6, S13EP7, S13EP8, S13EP9, S13EP10, S13EP11, S13EP12, S13EP13, S13EP14, S13EP15, S13EP16, S13EP17,S13EP18,S13EP19,S13EP20,S13EP21,S13EP22,S13EP23,S13EP24,
                                         S14EP1, S14EP2, S14EP3, S14EP4, S14EP5, S14EP6, S14EP7, S14EP8, S14EP9, S14EP10, S14EP11, S14EP12, S14EP13, S14EP14, S14EP15, S14EP16,S14EP17,S14EP18,S14EP19,S14EP20,S14EP21,S14EP22,S14EP23,S14EP24,
                                         S15EP1, S15EP2, S15EP3, S15EP4, S15EP5, S15EP6, S15EP7, S15EP8, S15EP9, S15EP10, S15EP11, S15EP12, S15EP13, S15EP14, S15EP15, S15EP16,S15EP17,S15EP18,S15EP19,S15EP20,S15EP21,S15EP22,S15EP23,S15EP24,
                                         S16EP1, S16EP2, S16EP3, S16EP4, S16EP5, S16EP6, S16EP7, S16EP8, S16EP9, S16EP10, S16EP11, S16EP12, S16EP13, S16EP14, S16EP15, S16EP16,S16EP17,S16EP18,S16EP19,S16EP20,S16EP21,S16EP22,S16EP23,S16EP24
)))

colnames(Ratings)
names(Ratings)[1] <- "Ratings"

##### Combining Code ######
NCISFull <- rbind(NcisS12, NcisS13, NcisS14, NcisS15, NcisS16)
NCISFull <- cbind(NCISFull, Ratings)
##### Cleaning #####
NCISFull$viewers <- as.double(NCISFull$viewers)
NCISFull$Ratings <- as.double(NCISFull$Ratings)
##### Creating NCIS CSV Files #####
write.csv((NCISFull), "NCIS_Dataset.csv")

library(readr)
NCISLA <- read_csv("NCISLA.csv")

NCISLA$production_code <- NULL

#install.packages("rvest")
#install.packages("tidyverse")
#install.packages("tidyr")
library(rvest)
library(stringr)
library(tidyverse)
library(tidyr)

############################ NCIS ##################################

NCISLAS1Rating <- read_html("https://www.imdb.com/title/tt1378167/episodes?season=1")

### S1 ###
S1EP1 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP2 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP3 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP4 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP5 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP6 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP7 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP8 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[8]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP9 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[9]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP10 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[10]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP11 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[11]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP12 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[12]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP13 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[13]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP14 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[14]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP15 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[15]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP16 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[16]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP17 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[17]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP18 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[18]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP19 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[19]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP20 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[20]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP21 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[21]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP22 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[22]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP23 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[23]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S1EP24 <- NCISLAS1Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[24]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()


NCISLAS2Rating <- read_html("https://www.imdb.com/title/tt1378167/episodes?season=2")

### S2 ###
S2EP1 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP2 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP3 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP4 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP5 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP6 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP7 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP8 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[8]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP9 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[9]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP10 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[10]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP11 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[11]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP12 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[12]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP13 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[13]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP14 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[14]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP15 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[15]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP16 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[16]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP17 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[17]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP18 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[18]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP19 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[19]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP20 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[20]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP21 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[21]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP22 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[22]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP23 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[23]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S2EP24 <- NCISLAS2Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[24]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()


NCISLAS3Rating <- read_html("https://www.imdb.com/title/tt1378167/episodes?season=3")

### S3 ###
S3EP1 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP2 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP3 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP4 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP5 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP6 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP7 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP8 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[8]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP9 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[9]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP10 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[10]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP11 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[11]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP12 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[12]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP13 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[13]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP14 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[14]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP15 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[15]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP16 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[16]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP17 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[17]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP18 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[18]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP19 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[19]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP20 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[20]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP21 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[21]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP22 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[22]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP23 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[23]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S3EP24 <- NCISLAS3Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[24]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()


NCISLAS4Rating <- read_html("https://www.imdb.com/title/tt1378167/episodes?season=4")

### S4 ###
S4EP1 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP2 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP3 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP4 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP5 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP6 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP7 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP8 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[8]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP9 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[9]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP10 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[10]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP11 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[11]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP12 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[12]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP13 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[13]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP14 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[14]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP15 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[15]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP16 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[16]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP17 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[17]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP18 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[18]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP19 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[19]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP20 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[20]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP21 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[21]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP22 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[22]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP23 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[23]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S4EP24 <- NCISLAS4Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[24]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()


NCISLAS5Rating <- read_html("https://www.imdb.com/title/tt1378167/episodes?season=5")

### S5 ###
S5EP1 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP2 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP3 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP4 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP5 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP6 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[6]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP7 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[7]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP8 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[8]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP9 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[9]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP10 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[10]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP11 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[11]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP12 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[12]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP13 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[13]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP14 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[14]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP15 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[15]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP16 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[16]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP17 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[17]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP18 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[18]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP19 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[19]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP20 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[20]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP21 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[21]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP22 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[22]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP23 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[23]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

S5EP24 <- NCISLAS5Rating %>%
  html_nodes(xpath = '//*[@id="episodes_content"]/div[2]/div[2]/div[24]/div[2]/div[2]/div[1]/span[2]') %>%
  html_text()

Ratings <- as.data.frame(as.double(cbind(S1EP1, S1EP2, S1EP3, S1EP4, S1EP5, S1EP6, S1EP7, S1EP8, S1EP9, S1EP10, S1EP11, S1EP12, S1EP13, S1EP14, S1EP15, S1EP16,S1EP17,S1EP18,S1EP19,S1EP20,S1EP21,S1EP22,S1EP23,S1EP24,
                                         S2EP1, S2EP2, S2EP3, S2EP4, S2EP5, S2EP6, S2EP7, S2EP8, S2EP9, S2EP10, S2EP11, S2EP12, S2EP13, S2EP14, S2EP15, S2EP16, S2EP17,S2EP18,S2EP19,S2EP20,S2EP21,S2EP22,S2EP23,S2EP24,
                                         S3EP1, S3EP2, S3EP3, S3EP4, S3EP5, S3EP6, S3EP7, S3EP8, S3EP9, S3EP10, S3EP11, S3EP12, S3EP13, S3EP14, S3EP15, S3EP16,S3EP17,S3EP18,S3EP19,S3EP20,S3EP21,S3EP22,S3EP23,S3EP24,
                                         S4EP1, S4EP2, S4EP3, S4EP4, S4EP5, S4EP6, S4EP7, S4EP8, S4EP9, S4EP10, S4EP11, S4EP12, S4EP13, S4EP14, S4EP15, S4EP16,S4EP17,S4EP18,S4EP19,S4EP20,S4EP21,S4EP22,S4EP23,S4EP24,
                                         S5EP1, S5EP2, S5EP3, S5EP4, S5EP5, S5EP6, S5EP7, S5EP8, S5EP9, S5EP10, S5EP11, S5EP12, S5EP13, S5EP14, S5EP15, S5EP16,S5EP17,S5EP18,S5EP19,S5EP20,S5EP21,S5EP22,S5EP23,S5EP24
)))

colnames(Ratings)
names(Ratings)[1] <- "Ratings"

##### Combining Code ######
NCISLA <- cbind(NCISLA, Ratings)

##### Cleaning #####
NCISLA$viewers <- as.double(NCISLA$viewers)
NCISLA$Ratings <- as.double(NCISLA$Ratings)


##### Creating NCIS CSV Files #####
write.csv((NCISLA), "NCISLA_Dataset.csv")

