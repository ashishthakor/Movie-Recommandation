# Movie-Recommandation

In this i make GUI with Tkinter and shared 1 csv file whichcontain movie list and features.

First you have to select movie and then you have to press apply to get similer movie.

But first you have to convert text file to csv file using this code:-

"""

import pandas as pd

dataframe1 = pd.read_csv("movie_file.txt")

dataframe1.to_csv('movie_list.csv', index = None)

"""
