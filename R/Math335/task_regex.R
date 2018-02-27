# regular expressions
library(tidyverse)
library(stringr)

# str_view() and str_all() take a character vector and a regular expression

x <- c("apple", "banana", "pear")
str_view(x, "an")
str_view(x, ".a.") # the dot '.' stands in place of any character except a newline

# '\' is an escape function for both strings and regex, and since we use strings to represent
# regular expressions, we need the double '\\'
str_view(c("abc", "a.c", "bef"), "a\\.c") # this finds the exact character 'a.c'
str_view(c("a\b", "abc", "a\\c"), "\\\\") # you need four backslashes \\\\ to find one '\'

x <- "a\\b"
writeLines(x) # this prints the characters in between the quotes

x <- c("apple and ants", "banana", "pear")
str_view(x, "^a") # this finds strings that begin with 'a'
str_view(x, "a$") # this finds strings that end with 'a'
x <- c("apple and ants", "apple", "banana", "pear")
str_view(x, "^apple$") # this finds the exact full string 'apple'


# this chapter is enormous so I'm going to stop here











