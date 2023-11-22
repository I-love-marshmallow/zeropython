a = '📚'
print(a, '3-1 一歩進むための準備')

name = input('your name?')
print(name + ', I hope everything is going well!')

print("Calculate the area")
height = float(input('Enter the height'))
width = float(input('Enter the width'))
print(f'The area is, {height * width}')

# this mark works as an comment

print (a,'3-2 条件分岐')

age = 3
if age < 18:
    print('no right for the election')


temprature = 40 
if temprature > 37.5:
    print('you have a posibillity of Covid')
    print('I will recommend going to the hospital')
elif temprature < 35.0:
    print ('You might be Hypothermia')
    print('I recommend going to the hospital')
else: 
    print("Your tempurature is moderate. However, alwasys note that tempurature is just one aspect of dignosing desease.")
print('Have a great day')

print(a,'3-3 論理演算子')

temprature = 40 
if (temprature > 37.5) or (temprature < 35.0):
    print('I will recommend going to the hospital')
else: 
    print("Your tempurature is moderate. However, alwasys note that tempurature is just one aspect of dignosing desease.")
print('Have a great day')
# Use () and (), so that make it more straightforward 


print(a, '3-4 処理の繰り返し')

print('while,', 'for,', 'range')
#for sentence is when the repeated count is limited 
#for while is unlmited 

i = 0 
while i < 5:
    print('wow')
    i += 1
# last sentence means i + 1, 変数は入力されるものでない

i = 0
for i in [1,2,3,4,5]:
    print(i)
#　Mario cart start dash

for i in range(10):
    print(i)

#break command,　変数の足し算 
total = 0 
for i in range (10):
    total += i
    if total > 20:
        break 
print(i, total)

total = 0 
for i in range (50):
    if i % 3 == 0:
        continue 
    print(i)
    total += i 

print('total is ', total) 

#ループ処理のネスト
#This generates a sequence of numbers starting from 1 and up to (but not including) 4. So, it represents the numbers 1, 2, and 3.

for a in range(1, 4):
    print('a=', a)
    for b in range (1,4):
        print ('b=', b)















