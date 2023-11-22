a = '📚'
print(a, '2-1 型と算術演習')

type(1)
type(-0.5)
type('hey')
type(False)

b = ((c := 2) * 2)
print(b)

d = 1.2 + 3 
print(d)
type(d)

e = 'heads up!'
print(e ,'-', 'float class could mistake ')

print(a, '2-2 文字列の扱い')

last_name = 'Tom'
middle_name = 'Jr'
first_name = 'Stewart'

name = last_name + middle_name + first_name 
print(name)

country = "USA "
states = 'Texas, '
the_city = "El paso, "
celsius = '30'
message = 'Tempurature in ' + the_city + states + country + 'is ' + celsius
print(message)

age = 22 
print(str(age) + "años")

price = 20 
print ('This is' + str(price) + 'bucks')

price = 50
print(f'This is {price} bucks')

yen = 150 
us_item = 500
print(f'This costs {us_item}')
print(f'For a dollar, the Japanese yen is {yen}') 
print(f'The charge will be {us_item * yen}')

print(2.5e6)


print (a, '2-3 リスト')

scores = (1,2,3,4,5)
print(scores[0])
print(scores[-2])

gender = ('male', 'female', 'others')
print(gender[1])

print(a, '2-4 モジュールの利用')

key_words = 'importsentence','Math_module', 'random_module'
print('key words are', key_words)


import random
assessment = ['Excellent', 'Nice', 'Bad']
print(random.choice(assessment)) 

destination = ['EU', 'Asia', 'Africa','America','North pole']
print(random.choice(destination))


















