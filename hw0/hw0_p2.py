# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:09:20 2021

@author: miffy
"""
dict1={}
movie=[]
filename = 'IMDB-Movie-Data.csv'
with open(filename, 'r') as f:  #匯入資料
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
               'Revenu(Millions)':row[9],
               'Meetascore':row[10]}
        movie.append(dict1)
        dict1={}


#第一題
def pb1():
    print('第一題')
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
        
        
#第二題
def pb2():
    print('第二題')
    list3=[]#所有'Revenue'
    
    for i in range(len(movie)):
        check=movie[i].get('Revenue(Millions)')
        if isinstance(check, str) and check!='':
            list3.append(float(movie[i].get('Revenue(Millions)')))
        else:
            list3.append(0.0)
            
    list3.sort(reverse=True)
    
    for i in range(len(movie)):
        if movie[i].get('Revenue(Millions)') == str(list3[0]):
            print(movie[i].get('Title'))
        
        
#第三題
def pb3():
    print('第三題')
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


#第四題
def pb4():
    print('第四題')
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

pb1()
pb2()
pb3()
pb4()


        
        
        

    
    
    
    
    
    
    
    