from tkinter import *
import pandas as pd
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def m_final(final_movie):
    def get_title_from_index(index):
        return df[df.index == index]["title"].values[0]

    def get_index_from_title(title):
        return int(df[df.title == title]["index"].values[0])
    #print(final_movie)
    #   Read CSV File
    df = pd.read_csv("movie_list.csv")
    #print(df.head())
    #print(df.columns)
        
    #   Select Features

    features = ['genres','keywords','cast','director','title']

    #   Create a column in DF which combines all selected features

    for feature in features:
        df[feature] = df[feature].fillna('')

    def combine_features(row):
        try:
            return row["title"]+" "+row['keywords']+" "+row['cast']+" "+row["director"]+" "+row["genres"]
        except:
            print("Error:", row)

    df["combined_features"] = df.apply(combine_features,axis=1)

    #print("Combined Features:", df["combined_features"].head())

    #   Create count matrix from this new combined column
    cv = CountVectorizer()

    count_matrix = cv.fit_transform(df["combined_features"])
    #print(count_matrix)
    
    #   Compute the Cosine Similarity based on the count_matrix
    cosine_sim = cosine_similarity(count_matrix)
    #print(cosine_sim)
    
    movie_user_likes = final_movie
    #print(movie_user_likes)

    #   Get index of this movie from its title
    try:
        movie_index = get_index_from_title(movie_user_likes)
        similar_movies =  list(enumerate(cosine_sim[movie_index]))

        #   Get a list of similar movies in descending order of similarity score
        sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)

        #   Print titles of first 50 movies
        i=4
        j=5
        for element in sorted_similar_movies:
            suggation_movie = Label(root , text=get_title_from_index(element[0]))
            if(i<=29):
                suggation_movie.grid(row=i,column=0)
            
            elif(i>29):
                suggation_movie.grid(row=j,column=1)
                j+=1

            

            #print(get_title_from_index(element[0]))
            i=i+1
            if i>54:
                break
    except:
        print("There is No Movie like",movie_user_likes)


movie_user_likes=pd.read_csv("movie_list.csv")
#print(temp)

# Create object
root = Tk()
  
# Adjust size
#root.geometry( "600x400" )
  
# Change the label text
def show():
    final_movie=clicked.get()
    label.config( text = "Press \"Apply\" to Get Similer Movie like "+clicked.get())
    #print(final_movie)
    button = Button( root , text = "Apply",command=lambda: m_final(final_movie) ).grid(row=3,column=0,columnspan=2,ipadx=30)
	
  
# Dropdown menu options
list1 = movie_user_likes['title'].tolist()
#print(list1)
#list1 = list(filter(None,list1))
#print(list1)
#list1 = [re.sub(r'[^a-zA-Z0-9]','',string) for string in list1]
#options = list1.sort()
options = list1
#print(options)
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( options[0] )
  
# Create Dropdown menu
'''label_head = label(root,text="Select Movie From Below DropDown List")
label_head.pack()'''

label1 = Label(root , text = "Select Movie From Drop Down And Press \"Select Movie Button\"")
label1.grid(row=0,column=0)

drop = OptionMenu( root , clicked , *options )
drop.grid(row=0,column=1,padx=30,ipadx=50)
  
# Create button, it will change label text
button = Button( root , text = "Select Movie" , command = show )
button.grid(row=1,column=0,columnspan=2,ipadx=30)
  
# Create Label
label = Label( root , text = " " )
label.grid(row=2,column=0,columnspan=2)

  
# Execute tkinter
root.mainloop()
