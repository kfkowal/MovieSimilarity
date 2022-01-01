# Movie similarity map

## the aim of this project is to create a map of points (points are representing movies (250 movies from top IMDB movie list are used)) where the closeness of points represents similarity between movies.

## You can this map to find the next movie to watch. For example lets say I've watched movie "Das Bot" recently and I really liked it, I can find where that movie is located on the map and then search for some other movies which are close to this one. Chances are that if I liked the first movie I will also like the movies that are simmilar to it.

# How simmilarity between movies is calculated:

## The [LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) model is used to divide movies into some latent topics. Data fed to model consists of textual descriptions of the movies from IMDB. The topics are latent, you can also change the number of topics to see different results.

## Based on that model vectors are assigned to movies, where those vectors represent how much given movie is likely to contain given topic.

## For example, lets say we have two movies **M1** and **M2** and the model generated containes 3 latent topics: **T1**, **T2** and **T3**

## the vectors assigned to movies would look something like that: **M1** : [0.5, 0 , 0.1] and **M2** : [0, 0, 0.8] which would indicate that both movies are quite different since they share only once topic but first movie contains much less of it.

## The vectors can have much higher dimensionality, for example one vector can have 100 topics. To achieve 2d map the multidimensional scaling is used

# The reflections
## The result is rather disappointing. The map is quite accurate sometimes, specially when it comes to war or sci-fi movies but for the most part it is not reliable. The main reason why I think this is happening is the small amount of data used, but I found it quite difficult to find good movie descriptions in large quantities.

# UWAGA
## Zapomniałem dodać jeszcze jednego mojego projektu do ankiety, znajduje się [tutaj](https://github.com/kfkowal/PAS_projekt)
