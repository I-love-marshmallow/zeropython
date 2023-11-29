a = '📚'

print (a, '4-1 オブジェクト指向')

a = 3 
id (a)
b = 3 
id (b)

print (a is b)

a = 10 
b = 10 
c = 5 
print(a == b)
print(a == c)

a = [1, 2, 4]
b = [1, 2, 4]
print(a is b)
print(a == b)
# [a == b True], [a is b False] 

a = b 
print(a is b)
print(a == b)
# [a == b True], [a is b True]

type('Hello')
type([2,4,6])

data = [1, 2, 3]
print(type(data))
print(type(data[0]))
# オブジェクト指向言語＝インスタンス　＆　クラスの概念

# Methods, meaning the function 

s = 'Hello, typhon'
m = 'Yeahhhhhhhhhh'
s.count('o')
m.count('h')
print (s.count('o'), m.count('h'))

a = '📚'
print(a, '4-2 文字列の操作')

print('文字列の基本操作')
'2021-03-01'.split('-')
print('2021-03-01'.split('-'))
print('Study Germany'.replace('Germany','Hungary'))

# lower()
# upper()
# find()
# split()
# replace()

print('Formatメソッドによる文字列の整形')

year = 1999
month = 12
day = 4 
message = 'Today is {}/{}/{}'.format(day, month, year)
print(message)

import math 
'円周率は{}'.format(math.pi)
'円周率は{:.3f}'.format(math.pi)

print ('円周率は{}'.format(math.pi))
print('円周率は{:.3f}'.format(math.pi))

print('{:,}円'.format(1200))
# "," means X,000,000....

print('{:>5}円'.format(999))
# make a blank 

print('in　演算子')

'オブジェクト' in 'pythonオブジェクト指向言語'
print('オブジェクト' in 'pythonオブジェクト指向言語')

print('4-3 リストとタプル')

#append(x) add 
#insert(i, x)
#remove(x) 
#pop() At the end of the object
#clear()
#index(x) 何番目か調べる
a = [3,4,5,6,7]
print(a.index(5))
#count(x)
#reverse()

#del 変数[index]
score = [30,40,50]
del score[-1]
print(score)

#+演算
list1 = 'human'
list2 = 'being'
list3 = list1 + list2 
print (list3)

#in演算子
data = ['apple','milk','soup']
print('apple' in data) 
print('beef' in data) 

#len関数 (要素の数を調べる)
scores = [1,2,3,4,5,6,50]
print(len(scores))

#sorted関数 並び替え
scores = [50,45,60,33,4]
scores = sorted(scores)
print(scores)

scores = sorted(scores, reverse=True)
print(scores)

#内包表記
data = [0,3,2,4,5]

data = []
for n in range(1, 11):
    data.append(2**n)
print(data)
# ２のN乗のNに１から１０までの整数が入る（From 2 to 2**11, 1024）

# Simple version 
data = [2**n for n in range(1, 11)]
print(data)

data = [str(n)+'月' for n in range (1,13)] 
print(data)

list = ['apple', 'banana', 'orange']
list2 = [s.upper() for s in list]
print(list2)

# 式　for 変数　in 反復可能なオブジェクト　if 条件式
data0 = ['apple', 'orange', 'avocado']
data1 = [s for s in data0 if s[0] == 'a']
print(data1)

data = [[1,2],[3,4,5]]
print(data[0])
# print [0] retrive the elements of box0, and [1] retrive the elements at index 1 within that sublist. 
print(data[0][1])

sample_data = 1,2,3,4,5

data = ('山田', '太郎','090-0000-0000')
a, b, c = data
print(a)
print(c)

print('📚', '4-4 辞書とセット')

print('⚪️辞書')
info = {'firstname':'Nick','lastname':'Smith','country':'US'}
print(info)

print(info.get('firstname'))
# 異なる点はNoneと表示される

#info.key()
for k in info.keys():
    print(k)

#info.values()
for v in info.values():
    print(v)

#info.items()
for i in info.items():
    print(i)

    #if you change i into k, v...
    for k, v in info.items():
        print(k, v)

info['phone'] = '090-0000-0000'
# if you want to delete, use 'del info['address']'

print(len(info))

print(info.get('phone'))

print('age' in info)
print('phone' in info)

print('⚪️SET') 
#複数のオブジェクトを格納できる点でリストに似ているが、『要素の重複を許さない』、「順序がない」という特徴を持つ。

print()
chars = {'a','b', 'c', 'a','b'}
print(chars)

data = [1,2,3]
s = set(data)
print(s)

#insubset ある要素全てが別のセットに含まれているかどうかを確認
set1 = {'a','b','c'}
set2 = {'b','c'}
print(set2.issubset(set1))
print(set1.issubset(set2)) 

set1 = {'a','b','c'}
set2 = {'a','b','d'}

#| 和(少なくともどちらか一方に含まれるもの)
#＆ 積(両方に含まれるもの)
#ー差（Set1にのみ含まれるものが出力される）
#^排他的論理和（どちらか一方だけにむくまれる要素からなるセットを得る）
print(set1 | set2) 
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)

print('📚 4-5 基本形の性質')

#　①　Mutable - list, dict, set 
m = [1,2,3,4,5]
print(id(m))
m.append(45)
print(id(m))

#　②　Immutable - int, float, bool. str, tuple 
t = (1,2,3)
print(id(t))
t = t + (5,6)
print(t)
print(id(t))

#①for文、リスト、タプル、辞書、セット
for c in 'Hello how are you':
    print(c)

                #(反復可能なオブジェクト)＝一つずつ順番に取り出せるもの
# list 
s = {'A','B','C'}
for i in s:
    print(i)

# Set 
info = {'firstname':'Jiro','lastname':'Smith', 'phone':'000-0000-000'}
for i in info:
    print(i)

s = 'Python'
print(s[3])
print(s[1:5]) #from 1 to 4 

import turtle

for i in range(10,301,10): 
    turtle.forward(i)
    turtle.left(90)

turtle.Screen().exitonclick()
turtle.bye()









