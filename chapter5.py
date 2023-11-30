print('📚 5-1 関数')

#関数を定義する（def構文）

def greet(name):
    print(f"Hello, {name}")

print(greet("John"))


def A():
    print('This is A')

print('We will call for A')
A()
print('We finished calling for A')

def B():
    print("No, sir")

def C():
    print("Are you hungry?")
    B()
    print('Are you sure?')
    B()

print('Dialog')
C()
#関数の時はprintは記入しない

print('📚 5-2 関数の引数')

def countdown():
    print("カウントダウンをします")
    counter = 5 
    while counter >= 0:
        print(counter)
        counter -= 1

countdown()

    #とある特定の数字から始めたい場合、countdown(3) & 関数のdef countdown（start）に設定する。

def countdown(start):
    print('関数が受け取った値：', start)
    print('カウントダウンをします')
    counter = start 
    while counter >= 0:
        print(counter)
        counter -= 1

countdown(3)
countdown(10)

    #とある特定の数字から特定の数字までを指定したい場合、countdown(5,3) 関数のdef countdown（start）countdown（end）に設定する。

def countdown(start, end):
    print('関数が受け取った値：', start)
    print('関数が受け取った値：', end)
    print('カウントダウンをします')
    counter = start 
    while counter >= end:
        print(counter)
        counter -= 1

countdown(11, 8) #キーワード引数　(end=1, start=5)is fine, too

# デフォルト引数、デフォルト値　def countdown(start, end=0)という。

# 可変長引数
print(2)
print(2,'abc')

# 可変長引数を持つ関数の定義　
    #def average (*args):
    #total = 0
    #for a in args

#可変長引数を持つ関数で受け取った値の平均を出力する
def average(*args):
    total = 0 
    for a in args:
        total += a 
        print(total / len(args))

average(50, 49, 30)

    #数字ではなく、キーワードの場合（**kwargs）
def print_data (**kwargs):
    for key, value in kwargs.items():
        print(f'キー：{key},値：{value}')

print_data(item='リンゴ',count=1, price=120)

print('📚, 5-3 関数の戻り方')
def circle_area(r):
    return r * r * 3.14

a = circle_area(2.5)
print('半径2.5の円の面積は', a)

#真偽値を返す関数
def is_positive(i):
    if i > 0:
        return True 
    else:
        return False 

a = -10;
if is_positive(a) == True:
    print('aは正の値')
else:
    print("aの値は負またはゼロ")

#短く書ける
def is_positive(i):
    return i > 0 

a = -10;
if is_positive(a):
    print('aの値は正です')
else:
    print('aの値は負またはゼロです')


#真偽値を返す関数
def is_positive(i):
    if i > 0:
        return True 
    else: 
        return False 

a = -10;
if is_positive(a) == True:
    print('aの値は正です')
else:
    print('aの値は負またはゼロです')

def get_two_numbers():
    return (2,3)

a,b = get_two_numbers()
print(a, b)

print('📚 5-4 高階関数とラムダ式')

def do_nothing():
    pass #何もしないという命令

print(type(do_nothing))

def print_price(price, func):
    print('The price is' + func(price))

def price_without_tax(price):
    return f'{price}Yen without tax'

def price_with_tax(price):
    return f'{int(price*1.1)}Yen including tax'

print_price(800, price_without_tax)
print_price(800, price_with_tax)

#Lambda式（高階関数が一行で書ける場合に　引数：戻り値　に記述したもの）
def print_price(price, func):
    print('The price is' + func(price))

print_price(800, lambda price: f'税抜き{price}円')
print_price(800, lambda price: f'税込{int(price*1.1)}円')



