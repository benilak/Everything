import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv("movies.csv")

movies["mpaa"] = movies.mpaa.apply(lambda v: v.strip())

#PartI:
    #1)
movies.rating.mean()
movies.rating.median()

    #2
movies[movies.mpaa=="PG-13"].year.min()

    #3
movies_mpaa = movies[movies.mpaa != ""]
movies_mpaa.plot.bar()

#PartII:
    #1)
movies_R = movies[movies.mpaa == "R"]

print(movies_R.columns)

print("Number of R-rated movies for each genre:")
print("Action: {}".format(movies_R.Action.value_counts()[1]))
print("Animation: {}".format(movies_R.Animation.value_counts()[1]))
print("Comedy: {}".format(movies_R.Comedy.value_counts()[1]))
print("Drama: {}".format(movies_R.Drama.value_counts()[1]))
print("Documentary: {}".format(movies_R.Documentary.value_counts()[1]))
print("Romance: {}".format(movies_R.Romance.value_counts()[1]))
print("Short: {}".format(movies_R.Short.value_counts()[1]))

genres = ["Action", "Animation", "Comedy", "Drama", "Documentary", "Romance", "Short"]
genre_R_counts = [644, 11, 916, 1723, 67, 440, 6]
R_counts = pd.DataFrame({"Count": genre_R_counts, "Genre": genres})
R_counts.plot.bar(x="Genre", y="Count", title="Number of R-rated Movies by Genre")

    #2)
movac = movies[(movies.Action==1) | (movies.Comedy==1)]
movac = movac[movac.budget != " NA"]
movac = movac.sort_values("year")

movac.budget = movac.budget.astype(int)

movac_hist = plt.hist(movac.budget[movac.Comedy==1], alpha=0.5, bins=40)
movac_hist = plt.hist(movac.budget[movac.Action==1], alpha=0.5, bins=40)
movac_hist = plt.xlim((0,1e8))
movac_hist = plt.title("Histograms of Budget for Action & Comedy Genres")
movac_hist = plt.xlabel("Budget (in $100 millions)")
movac_hist = plt.ylabel("Frequency")
movac_hist = plt.legend(["Comedy", "Action"])
plt.show(movac_hist)

    #3)
movplot, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(7, sharex=True, sharey=True)
ax1.hist(movies.year[movies.Action==1], bins=50, color='Red')
ax2.hist(movies.year[movies.Animation==1], bins=50, color='Orange')
ax3.hist(movies.year[movies.Comedy==1], bins=50, color='Gold')
ax4.hist(movies.year[movies.Drama==1], bins=50, color='Green')
ax5.hist(movies.year[movies.Documentary==1], bins=50, color='Blue')
ax6.hist(movies.year[movies.Romance==1], bins=50, color='Indigo')
ax7.hist(movies.year[movies.Short==1], bins=50, color='Violet')
ax1.set_ylabel("Action")
ax2.set_ylabel("Animation")
ax2.yaxis.set_label_position("right")
ax3.set_ylabel("Comedy")
ax4.set_ylabel("Drama")
ax4.yaxis.set_label_position("right")
ax5.set_ylabel("Documentary")
ax6.set_ylabel("Romance")
ax6.yaxis.set_label_position("right")
ax7.set_ylabel("Short")
ax7 = plt.xlim((1920,2005))
movplot.suptitle("Frequency of Movie Genre Over Time")
plt.show(movplot)


#PartIII:
    #1)
movies_long = movies[movies.length >= 150]
movies_shorter = movies[movies.length < 150]

movies_long.rating.mean()
movies_shorter.rating.mean()

    #2)
movies_high = movies[movies.rating >= 7.7]
movies_low = movies[movies.rating <= 4]

sum(movies_high.mpaa.value_counts())
sum(movies_low.mpaa.value_counts())

movies_high.mpaa.value_counts()
movies_low.mpaa.value_counts()


not_ancient = movies[movies.year > 1960]
not_ancient.sort_values("year")
graph = plt.bar(not_ancient.rating, not_ancient.budget)
plt.show(graph)