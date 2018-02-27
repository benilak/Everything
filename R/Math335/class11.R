# Class 11

library(tidyverse)
library(dplyr)
library(buildings)

# type buildings:: to see what data sets the package contains

View(buildings0809)
View(climate_zone_fips)
View(permits)
View(restaurants)

# tip: check if values are in a vector
c(1,3,6,2,7,9,5) %in% c(3,6)
# returns boolean vector: [1] FALSE  TRUE  TRUE FALSE FALSE FALSE FALSE

