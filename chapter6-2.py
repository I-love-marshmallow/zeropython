#インスタンスに依存しないクラスメソッド
class SimpleCalc:
    @classmethod #@classmethodを使用する
    def get_triangle_area(cls, base, height): #クラスめメソッドの定義
        return base * height / 2 

print(SimpleCalc.get_triangle_area(10, 5))

#__Name__変数

class NameCard: #NameCardクラスの定義
    def __init__(self, name):
        self.name = name 

a = NameCard("James Smith")#クラスが適切に定義されていることを確認するためのコード
print(a.name)

#別のコードで引用する時にJames Smithではなく一般化するとき

class NameCard:
    def __init__(self, name):
        self.name = name

from chapter6 import NameCard

if __name__ == "__main__":
    a = NameCard('JohnSmith')
    print(a.name)

print('6-3 継承')

# class A (they are passed down object class)
# class b(A) (B is subclass of A)

from chapter6 import StudentCard

class IStudentCard(StudentCard):
    def __init__(self, id, name, nationality):
        self.nationality = nationality 
        super().__init__(id, name) 

# Override (If func is overlaped by subclass, superclass will be overwritten)

print('super keyword')

from chapter6 import StudentCard

class IStudentCard(StudentCard):
    def __init__(self, id, name, nationality):
        self.nationality = nationality
        super().__init__(id, name)

    def print_info(self):
        print(f'国籍: {self.nationality}')
        print(f'学籍番号: {self.id}')
        print(f'氏名: {self.name}')

from chapter6 import IStudentCard

a = IStudentCard(2345, 'Jhon Smith', "British")
a.print_info()





