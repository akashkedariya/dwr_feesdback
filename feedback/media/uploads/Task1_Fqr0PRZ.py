#1===============
# a = [1, 2, 3]
# b = [4, 5, 6]
# list = []
# for i in range(0, len(a)):                      #i = 0,1,2
#     list.append(a[i] + b[i])
# print(list)
#-------------
# result = map(lambda x, y: x + y, a,b)         #====res = map(lambda(i, j): i + j, zip(a,b))
# print(list(result))

# lambda:
# [5, 7, 9]


#2========
# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[3:5])


#3========
# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[-4:-2])


#4========
# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[3:5])


#5=======
# name = "Good Name"
# aa = list(name)
# print(aa)

#['G', 'o', 'o', 'd', ' ', 'N', 'a', 'm', 'e']


#5=======
# name = ['G', 'o', 'o', 'd', ' ', 'N', 'a', 'm', 'e']
# string = "".join(name)
# print(string)
#-------------------

# def string(name):
#     ss = ""    
#     for i in name:
#         ss = ss + i
#     return ss
# print(string(name))        

#"Good Name"


#6=======
# d = {'a':1, 'b':2, 'c':3, 'd':4}
# # x = list(d.items())
# # x = d.items()
# print(x)

#[('a', '1'), ('b', '2'), ('c', '3'), ('d', '4')]


#7==========
# d = {'a':1, 'b':2, 'c':3, 'd':4}
# a = []
# d.pop('d')
# x = tuple(d.keys())
# y = tuple(d.values())
# a.insert(0,x)
# a.insert(1,y)
# print(a)

# [('a', 'b', 'c'), (1, 2, 3)]


#8====== 
# a = [1, 2, 3, 4, 5]
# b = []
# for i in a:
#     if i==4:
#         continue
#     b.append(i)
# print(b,end=' ')

# [1, 2, 3, 5]


#9=========
# b = [10, 11, 12]
# a = [1, 2, 3, 4, 5] 
# a[3] = b
# print(a)        

# [1, 2, 3, [10, 11, 12], 4, 5]


#10=======
# b =[9]
# a = [1, 2, 3, [10, 11, 12], 4, 5]
# a[3].insert(1,9)
# print(a)

# [1, 2, 3, [10, 9, 11, 12], 4, 5]


#11=======
# a = [1, 2, 3, [10, 9, 11, 12], 4, 5]
# a[3].pop(0)
# print(a)

# [1, 2, 3, [9, 11, 12], 4, 5]


#12========
# name = "Good Name"
# a = name.split()
# a.reverse()
# print(' '.join(a))
#---------------------------
# b = []
# a =list(name)
# for i in a:
#     b.insert(0,i)
# # print(b)
# def string(b):
#     str = ""
#     for x in b:
#         str = str + x
#     return str   
# z = string(b)
# print(z)

# Name Good


#13==========
# d = {'a':1, 'b':2, 'c':3, 'd':4}
# d = {'a':1, 'b':2, 'c':3, 'd':4}
# d['e'] = [1, 2, 3]
# print(d)

# {'a':1, 'b':2, 'c':3, 'd':4, 'e': [1, 2, 3]}

#14===========
# l = [1, 2, 3, 4, 5]
# fac = 1
# for i in l:
#     fac = fac*i
# print(fac)  
# 120

#15=========
# l = [10, 20, 30, 40, 50]
# res = list(enumerate(l))
# print(res)
#------------------------
# a = []
# for i in range(0,5):
#     # print(a)
#     a.append(i)

# x = tuple(a)
# y = tuple(l) 
# z = zip(x,y)
# print(list(tuple(z)))  
# ----------------------
# b = []
# for i in range(0,len(l)):
#     # b.append((i,l[i]))
#     b.append({i:l[i]})
# print(str(b))  

# [(0, 10), (1, 20), (2, 30), (3, 40), (4, 50)]


#16==============
# l = [10, 20, 30, 40, 50]
# a = []
# b = [] 
# for i in l:
#     s= i//2
#     a.append(s)   
# for i in range(0,len(a)):
#     b.append((i,a[i]))
# print(str(b))

# divide by 2
# [(0, 5), (1, 10), (2, 15), (3, 20), (4, 25)]



#17===========
# l = [60,80,20, 30, 40, 50]
# print(min(l))
#------
# l.sort()
# print(l[0])
#------
# min = l[0]
# for val in l:
#     if val < min:
#         min = val
# print(min)
# Find Min: 10

#18============
# l = [10, 20, 30, 40, 50]
# # print(max(l))
# #----------
# # l.sort()
# # print(l[-1])
# #----------     
# max = l[0]
# print(max) 
# for i in range(0, len(l)): 
#    print(l[i]) 
#    if(l[i] > max):  
#        max = l[i];  
         
# print('maximum Element : ',max)

# Find Max: 50


#19==========
# range: from 1 to 5
# a = []
# for i in range(1,5):
#     a.append(i)
# print(a)

# [1, 2, 3, 4]


#19=============
# range: from 1 to 5, increment by 0.5
# for i in range(1,5):
#     print(i,i+0.5,end=" ")

# [1, 1.5, 2, 2.5, 3, 3.5, 4]


#20===========
# range: from 1 to 100
# for i in range(1,100):
#     if i%2 == 0:
#         print(i,end=' ')

# Find even


#21===========
# range: from 1 to 100
# for i in range(1,100):
#     if i%2 == 1:
#         print(i,' ')

# Find odd


#22==========
# a = (1, 2, 3)
# b = (4, 5, 6)
# # #-------
# # # print(dict(zip(a,b)))
# # #-------
# z = { }
# for index, value in enumerate(a):
#     # print(b[index])
#     # print(a[index])
#     z[value] = b[index]
# print(z) 

# {1: 4, 2: 5, 3: 6}


#23===========
# l = [1, 2, 3, False, 4]
# for i in l:
#     if i == False:
#         print(i)

#False


#24==========
# l = [1, 2, 3, False, 4]
# for i in l:
#     if i == False:
#         print(True)

# True

#25=========Pending---No output
# l = [1, 2, 3, False, 4]


#26=====Pending====Not know
# [(1, 10), (2, 20), (3, 30), (1, 40), (3, 50), (4, 60), (5, 80)]

# list = [(1, 10), (2, 20), (3, 30), (1, 40), (3, 50), (4, 60), (5, 80)]
# res = {}
# for k, v in list:
#     print(k,v)
#     res[k] = res.get(k, 0) + v
#     # print(res[k])
#     # print(v)
# print(res)

# {1: 50, 2: 20, 3: 80, 4: 60, 5:80}


#27=========
# l = [1, 2, 3, 1, 2, 1,2, 3, 2 ,5, 6]
# a = []
# for i in l:
#     if i not in a:
#         a.append(i)
# print(a,end= ' ')

# [1, 2, 3, 5, 6]


#28===========
# l = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# b = []
# c = []
# b1 = l[0][1]
# b2 = l[1][1]
# b3 = l[2][1]
# bb = b1, b2, b3
# for x in bb:
#     c.append(x)
# # print(c) 

# # #--------------
# a1 = l[0][1]
# a2 = l[1][1]
# a3 = l[2][1]
# aa = a1 ,a2 ,a3
# for i in aa:
#     b.append(i*2)
# # print(b)

# res = dict(zip(c,b))
# print(res)

# {2: 4, 5: 10, 8: 16}


#29==========
# l = [1, 2, 3, 4, 5, 6]
# a = []
# for i in l:
#     if i%2 == 0:
#         a.append(i)
# print(a)

# Using build in: Divind by 2
# [2, 4, 6]


#30==========
# a = []
# l = [1, 2, 3, 4, 5]
# for i in l:
#     a.append(i*2)
# print(a)

# using build in: [2, 4, 6, 8, 10] multiply by 2
