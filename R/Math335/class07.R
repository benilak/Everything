# in-class notes 01-30-18

library(tidyverse)
library(dplyr)

faithful %>%
  filter(!is.na(waiting)) %>%
  mutate(waiting_group = case_when(waiting < 67 ~ " < 67 min",
                                   waiting >= 67 ~ " > 67 min")) %>%
  ggplot(aes(x = eruptions, fill = waiting_group)) + 
  geom_histogram(color = "white") +
  theme_bw() +
  labs(x = "Duration of eruption (minutes)", 
       y = "Number of Observations")

faithful %>%
  mutate(waiting_group = case_when(waiting < 67 ~ " < 67 min",
                                   waiting >= 67 ~ " > 67 min")) %>%
  ggplot(aes(x = eruptions, fill = waiting_group)) + 
  geom_histogram(color = "white") +
  scale_fill_brewer(type = "qual") +
  theme_bw() + theme(legend.position = "bottom") +
  labs(x = "Duration of eruption (minutes)", 
       fill = "Duration\nof Wait", y = "Number of Observations")

View(faithful)

faithful %>%
  mutate(waiting_group = case_when(waiting < 67 ~ " < 67 min",
                                   waiting >= 67 ~ " > 67 min")) %>%
  ggplot(aes(waiting, eruptions)) + 
  geom_hex() +
  geom_smooth(method = "lm", color = "red")
  
         