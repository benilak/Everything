# in-class task

faithful %>%
  ggplot(aes(x = eruptions)) + 
  geom_histogram(color = "white") +
  theme_bw() +
  labs(x = "Duration of eruption (minutes)", 
       y = "Number of Observations")
View(faithful)