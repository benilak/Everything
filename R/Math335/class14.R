library(tidyverse)
library(rio)
library(stringr)
library(stringi)


bom <- read_csv('http://scriptures.nephi.org/downloads/lds-scriptures.csv.zip')


scriptures <- import("http://scriptures.nephi.org/downloads/lds-scriptures.csv.zip")
bm <- scriptures %>% filter(volume_short_title == "BoM")

# for loops part
verse <- read_lines("https://byuistats.github.io/M335/data/2nephi2516.txt")
names <- import("https://byuistats.github.io/M335/data/BoM_SaviorNames.rds")

for(i in names){
  
}









