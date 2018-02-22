import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("movies.csv")

print(data)

hist = data.year.hist()

#plt.show()

movies_90s = data[(data.year >= 1990) & (data.year < 2000)]
print(movies_90s.rating.min())
print(movies_90s.rating.median())
print(movies_90s.rating.max())

data.mpaa.value_counts()


def cleanup_rating(old):
    new = old.strip()
    return new

mpaa_rating = " PG"
clean_rating = cleanup_rating(mpaa_rating)

print(mpaa_rating)
print(clean_rating)


data.mpaa.apply()


def cleanup_rating(v): return v.strip()



data["mpaa_clean"] = data.mpaa.apply(lambda v: v.strip())

data.mpaa_clean.value_counts()