# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 23:02:49 2021

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
        
def check_Emma(dic) :#判斷有沒有Emma
    check=0
    temp=dic.get('Actors').split('| ')
    for i in temp:
        if i == 'Emma Watson':
            check=1
    return check

sum=0.0
time=0
for i in range(len(movie)):
    if check_Emma(movie[i]):
        sum += float(movie[i].get('Rating'))
        time += 1
print(sum/time)