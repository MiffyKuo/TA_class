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

director=[]
dir_act=[]
def is_in_director(name):
    for i in director:
        if i == name:
            return True
    return False

for i in range(len(movie)):
    #如果movie.get('Director')不再Director裡，就append進director
    if not(is_in_director(movie[i].get('Director'))):
        director.append(movie[i].get('Director'))
        
for i in director:
    dir_act.append([i,[],0])

for i in range(len(movie)):
    for j in range(len(dir_act)):
        if dir_act[j][0] == movie[i].get('Director'):
            dir_act[j][1] += movie[i].get('Actors').split('|')
num=[]#所有導演合作過的演員數量
for i in range(len(dir_act)):
    #消除重複演員
    dir_act[i][1] = list(set(dir_act[i][1]))
    #更新演員數量
    dir_act[i][2] = len(dir_act[i][1])
    
    num.append(dir_act[i][2])

num.sort(reverse=True)

for i in range(3):
    for j in range(len(dir_act)):
        if num[i] == dir_act[j][2]:
            print(dir_act[j][0])
            dir_act[j][2] = 0 #避免再次搜尋到該導演
            break
