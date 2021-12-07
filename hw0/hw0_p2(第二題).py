# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 23:02:17 2021

@author: miffy
"""

dict1={}
movie=[]
filename = 'IMDB-Movie-Data.csv'
with open(filename, 'r') as f:
    for line in f:
        row = line.split(',')
        if row[0] == 'Rank':
            continue
        dict1={'Rank':row[0],
               'Title':row[1],
               'Genre':row[2],
               'Director':row[3],
               'Actors':row[4],
               'Year':row[5],
               'Runtime(Minutes)':row[6],
               'Rating':row[7],'Votes':row[8],
               'Revenue(Millions)':row[9],
               'Meetascore':row[10]}
        movie.append(dict1)
        dict1={}
list3=[]#所有'Revenue'

for i in range(len(movie)):
    if movie[i].get('Revenue(Millions)')!='':
        list3.append(float(movie[i].get('Revenue(Millions)')))
    else:
        list3.append(0.0)
        
list3.sort(reverse=True)

for i in range(len(movie)):
    if movie[i].get('Revenue(Millions)') == str(list3[0]):
        print(movie[i].get('Title'))