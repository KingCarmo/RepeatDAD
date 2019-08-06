##### NCIS S12 #####
library(htmltab)

url6 <- "https://en.wikipedia.org/wiki/NCIS_(season_12)"

NcisS12 <- htmltab(doc = url6, which = 4)
View(NcisS12)

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
colnames(NcisS12)[3] <- "us_viewers_in_millions"
colnames(NcisS12)[6] <- "number_in_series"

NcisS12 <- NcisS12[,c(5,6,7,1,2,3,4)]
View(NcisS12)

##### NCIS S13 #####
library(htmltab)

url7 <- "https://en.wikipedia.org/wiki/NCIS_(season_13)"

NcisS13 <- htmltab(doc = url7, which = 3)
View(NcisS13)

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
colnames(NcisS13)[3] <- "us_viewers_in_millions"

NcisS13 <- NcisS13[,c(5,6,7,1,2,3,4)]
View(NcisS13)

##### NCIS S14 #####
library(htmltab)

url8 <- "https://en.wikipedia.org/wiki/NCIS_(season_14)"

NcisS14 <- htmltab(doc = url8, which = 3)
View(NcisS14)

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
colnames(NcisS14)[3] <- "us_viewers_in_millions"

NcisS14 <- NcisS14[,c(5,6,7,1,2,3,4)]
View(NcisS14)

##### NCIS S15 #####
library(htmltab)

url9 <- "https://en.wikipedia.org/wiki/NCIS_(season_15)"

NcisS15 <- htmltab(doc = url9, which = 3)
View(NcisS15)

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
colnames(NcisS15)[3] <- "us_viewers_in_millions"

NcisS15 <- NcisS15[,c(5,6,7,1,2,3,4)]
View(NcisS15)

##### NCIS S16 #####
library(htmltab)

url10 <- "https://en.wikipedia.org/wiki/NCIS_(season_16)"

NcisS16 <- htmltab(doc = url10, which = 3)
View(NcisS16)

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
colnames(NcisS16)[3] <- "us_viewers_in_millions"

NcisS16 <- NcisS16[,c(5,6,7,1,2,3,4)]
View(NcisS16)


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


NCISS12S16Rating <- as.data.frame(as.double(cbind(S12EP1, S12EP2, S12EP3, S12EP4, S12EP5, S12EP6, S12EP7, S12EP8, S12EP9, S12EP10, S12EP11, S12EP12, S12EP13, S12EP14, S12EP15, S12EP16,S12EP17,S12EP18,S12EP19,S12EP20,S12EP21,S12EP22,S12EP23,S12EP24,
                                                 S13EP1, S13EP2, S13EP3, S13EP4, S13EP5, S13EP6, S13EP7, S13EP8, S13EP9, S13EP10, S13EP11, S13EP12, S13EP13, S13EP14, S13EP15, S13EP16, S13EP17,S13EP18,S13EP19,S13EP20,S13EP21,S13EP22,S13EP23,S13EP24,
                                                 S14EP1, S14EP2, S14EP3, S14EP4, S14EP5, S14EP6, S14EP7, S14EP8, S14EP9, S14EP10, S14EP11, S14EP12, S14EP13, S14EP14, S14EP15, S14EP16,S14EP17,S14EP18,S14EP19,S14EP20,S14EP21,S14EP22,S14EP23,S14EP24,
                                                 S15EP1, S15EP2, S15EP3, S15EP4, S15EP5, S15EP6, S15EP7, S15EP8, S15EP9, S15EP10, S15EP11, S15EP12, S15EP13, S15EP14, S15EP15, S15EP16,S15EP17,S15EP18,S15EP19,S15EP20,S15EP21,S15EP22,S15EP23,S15EP24,
                                                 S16EP1, S16EP2, S16EP3, S16EP4, S16EP5, S16EP6, S16EP7, S16EP8, S16EP9, S16EP10, S16EP11, S16EP12, S16EP13, S16EP14, S16EP15, S16EP16,S16EP17,S16EP18,S16EP19,S16EP20,S16EP21,S16EP22,S16EP23,S16EP24
)))

colnames(NCISS12S16Rating)
names(NCISS12S16Rating)[1] <- "AllNCISRatings"

##### Combining Code ######
NCISFull <- rbind(NcisS12, NcisS13, NcisS14, NcisS15, NcisS16)
NCISFull <- cbind(NCISFull, NCISS12S16Rating)
##### Creating NCIS CSV Files #####
write.csv((NCISFull), "NCIS_Dataset.csv")