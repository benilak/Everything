#

dat %>%
  filter(!is.na(bf.type.4), bf.type.4 != "none", wasting != "no group", 
         month_of_age %in% c(1:6,seq(8,24, by = 2)), 
         !country %in% c("Brazil", "Peru", "South Africa", "Tanzania")) %>%
  mutate(`BF Status 4 months` = 
           factor(bf.type.4, levels = c("exclusive", "predominant", "partial")),
         days = month_of_age*30.25) 
#

library(iris)

iris %>%
  arrange(Sepal.Length) %>%
  slice(1:6) 

testdat <- iris %>% 
  select(Petal.Width)

iris %>%
  group_by(Species) %>%
  summarise(n = n(), Sepal.Width.mean = mean(Sepal.Width))

iris %>%
  group_by(Species) %>%
  summarise_all(c(mean, sd))




