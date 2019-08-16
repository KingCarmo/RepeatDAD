#install.packages("rvest")
library(rvest)
library(stringr)
library(htmltab)

##### Gathering Data ######

##### Suits season 2 ######
library(htmltab)

url2 <- "https://en.wikipedia.org/wiki/Suits_(season_2)"

SuitsS2 <- htmltab(doc = url2, which = 3)
View(SuitsS2)

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
colnames(SuitsS2)[4] <- "us_viewers_in_millions"

SuitsS2 <- SuitsS2[,c(6,1,7,2,3,4,5)]

##### Suits season 3 ######
library(htmltab)

url3 <- "https://en.wikipedia.org/wiki/Suits_(season_3)"

SuitsS3 <- htmltab(doc = url3, which = 5)
View(SuitsS3)

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
colnames(SuitsS3)[4] <- "us_viewers_in_millions"

SuitsS3 <- SuitsS3[,c(6,1,7,2,3,4,5)]

##### Suits season 4 ######
library(htmltab)

url4 <- "https://en.wikipedia.org/wiki/Suits_(season_4)"

SuitsS4 <- htmltab(doc = url4, which = 4)
View(SuitsS4)

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
colnames(SuitsS4)[4] <- "us_viewers_in_millions"

SuitsS4 <- SuitsS4[,c(6,1,7,2,3,4,5)]

##### Suits season 5 ######
library(htmltab)

url5 <- "https://en.wikipedia.org/wiki/Suits_(season_5)"

SuitsS5 <- htmltab(doc = url5, which = 3)
View(SuitsS5)

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
colnames(SuitsS5)[4] <- "us_viewers_in_millions"

SuitsS5 <- SuitsS5[,c(6,1,7,2,3,4,5)]

##### Suits season 6 ######
library(htmltab)

url6 <- "https://en.wikipedia.org/wiki/Suits_(season_8)"

SuitsS6 <- htmltab(doc = url6, which = 3)
View(SuitsS6)

rownames(SuitsS6) <- c(1:16)

SuitsS6$`Time slot (EST)` <- NULL
SuitsS6$`Rating(Adults 18â€“49)` <- NULL
SuitsS6$`18-49 Rankon Cable`<- NULL
SuitsS6$`Weekly rank` <- NULL

SuitsS6["season"] <- 6
SuitsS6$season <- as.integer(SuitsS6$season)

SuitsS6["name"] <- "Suits"

colnames(SuitsS6)[1] <- "number_in_series"
SuitsS6$number_in_series<- c(77:92)
SuitsS6$number_in_season <- c(1,2,3,4,6,6,7,8,9,10,11,12,13,14,15,16)
colnames(SuitsS6)[2] <- "title"
colnames(SuitsS6)[3] <- "original_air_date"
colnames(SuitsS6)[4] <- "us_viewers_in_millions"

SuitsS6 <- SuitsS6[,c(6,1,7,2,3,4,6)]

##### Creating Suits CSV Files #####
SuitsAllRating <- rbind (Season2Rating, Season3Rating, Season4Rating, Season5Rating, Season6Rating)
write.csv(rbind(Season1Suits, Season2Suits, Season3Suits, Season4Suits, Season5Suits), "Suits_Dataset.csv")


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

NcisS12$number_in_series <- c(1:24)
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

NcisS13$number_in_series <- c(25:48)
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

NcisS14$number_in_series <- c(49:72)
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

NcisS15$number_in_series <- c(73:96)
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

NcisS16$number_in_series <- c(73:96)
NcisS16$number_in_season <- c(1:24)
NcisS16 <- NcisS16[,-c(1)]
colnames(NcisS16)[1] <- "title"
colnames(NcisS16)[2] <- "original_air_date"
colnames(NcisS16)[3] <- "us_viewers_in_millions"

NcisS16 <- NcisS16[,c(5,6,7,1,2,3,4)]
View(NcisS16)

write.csv(rbind(NcisS12, NcisS13, NcisS14, NcisS15, NcisS16), "NCIS_Dataset.csv")

