# Class Meeting 10

util <- read_csv("https://byuistats.github.io/M335/data/building_utility_values.csv", 
                 col_types = cols(timestamp = col_datetime(format = "%m%.%d%.%Y %H:%M"),
                                   startdate = col_date(format = "%m%.%d%.%Y"), 
                                   enddate = col_date(format = "%m%.%d%.%Y")))

util2 <- util %>%
  select(2:4, contains("water"), contains("building")) %>%
  separate(building_id, c("state", "id"), sep = 2) %>%
  separate(enddate, c("year", "month", "day"), sep = "-", remove = FALSE)

buildings_by_state <- util2 %>%
  group_by(state) %>%
  summarise(count = n_distinct(id))
View(buildings_by_state)  

util2 %>%
  ggplot() +
  geom_line(aes(x = timestamp, y = total_potable_water_gal)) +
  facet_grid(id ~ .)

util2 %>%
  





         