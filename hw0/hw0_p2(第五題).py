# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 22:00:09 2021

@author: miffy
"""

dict1={}
movie=[]
filename = 'IMDB-Movie-Data.csv'
filename = 'test.csv'
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

actor=[]#不重複演員名單
result=[]
for i in range(len(movie)):
    actor += movie[i].get('Actors').split('|')
actor = list(set(actor))

for i in range(len(actor)):
    result.append([actor[i],[],0])

for i in range(len(movie)):
    for j in range(len(actor)):
        


















