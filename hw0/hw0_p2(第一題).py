# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 23:01:39 2021

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



list1=[]#符合2016的dict
list2=[]#2016的'Rating'

for i in range(len(movie)):
    if movie[i].get('Year') == '2016':
        list1.append(movie[i])
        list2.append(float(movie[i].get('Rating')))
list2.sort(reverse=True)

for i in range(len(list1)):
    if list1[i].get('Rating') == str(list2[0]):
        print(list1[i].get('Title'))
    if list1[i].get('Rating') == str(list2[1]):
        print(list1[i].get('Title'))
    if list1[i].get('Rating') == str(list2[2]):
        print(list1[i].get('Title'))