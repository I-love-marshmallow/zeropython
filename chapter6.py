print('6-1 新しいクラスを作る')
#学生証
#インスタンス変数を持つクラスの定義

class StudentCard:
    pass 

a = StudentCard()

print(type(a))

class StudentCard:
    def __init__(self):   #初期化メソッドです
        print('初期化のメゾッド内の処理です')

a = StudentCard()
b = StudentCard() 

#インスタンス変数を持つクラス, self.変数名　= 値

class StudentCard:
    def __init__(self):
        print('初期化メソッド内の処理です')
        self.id = 0 
        self.name = 'Not named'

a = StudentCard()
b = StudentCard()


a.id = 1234 
a.name = 'Emily'
b.id = 1234 
b.name = 'John'

print(f'a.id:{a.id}, a.name:{a.name}')
print(f'b.id:{b.id}, b.name:{b.name}')

# 初期設定でそれぞれの値を設定すれば後から変更する手間を省ける

            #def __init__(self, id, name):
                #self.id = id 
                #self.name = name 

            #a = StudentCard(1111, 'James')
            #b = StudentCard(1111, 'Emily')

class StudentCard:
    school_name = 'U of Tokyo' #クラス変数
    def __init__(self, id, name): #インスタンス変数
        self.id = ifself.name = name   

print(StudentCard.school_name)

print('6-2 メソッドの定義') 
#インスタンスには情報格納だけではなく、処理を実行する機能を持たせることもできる

class StudentCard: #initialization method
    def __init__(self, id, name):
        self.id = id
        self.name = name 

    def print_info(self): #print_info method
        print('学籍番号:', self.id)
        print('学籍番号：', self.name)

a = StudentCard(1234, 'Emily')
b = StudentCard(1235, 'Ruis')
a.print_info()
b.print_info()

print('You can control access from external w/ __')

class StudentCard: #外部からアクセスできない仕組み
    def __init__(self, id, name):
        self.__id = id 
        self.__name = name  

    def get_name(self):#名前を外部に公開できる設定
        return self._name 
    
    def get_id(self): # same function with id
        return self.__id 

a = StudentCard(1111, 'Jenny')
#print(a.__id)
#print(a.__name)

print(a.get__id())　#get_idの方を使用して情報を公開する（設定を変更を許可しない）
print(a.get__name())









