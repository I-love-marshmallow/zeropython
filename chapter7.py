print('7-1 発展と応用')
#　例外処理(文法があってても問題なく動作するとは限らない)
# 例外＝エラー

print('a ÷ b の計算をします')
a = input('aの値を入力してください：　')
b = input('bの値を入力してください：　')
c = float(a) / float(b)
print('答えは', c)

# 例外処理（問題が発生しても処理を続けるように設定）

#try: 本来実行したい処理（例外が発生する可能性がある）
#except:　例外が発生した時の処理

print('a ÷ b の計算をします')
try:
    a = input('aの値を入力してください: ')
    b = input('bの値を入力してください: ')
    c = float(a) / float(b)
    print('答えは', c)
except:
    print('入力が適切ではありません')

print('処理を終わります')

print('7-2 テキストファイルの読み書き')


print('How to open file 1')
# データ集計から有用な情報を抽出するための一歩はテキストファイルの読み書きを行えるようにすること
f = open('data/visitor_record.txt', 'r', encoding='UTF-8')　#ファイルを開き、ファイルオブジェクトを取得
lines = f.readlines()　#ファイルの中身を読み込む

for line in lines: #一行ずつ変数lineに取り出して処理する
    if '東京都'in line:　#東京都という文字列を含むか判定
        print(line,replace('¥n','')) #末尾の改行を削除して出力する

f.close() # Close file 

# r(読み込み用に開く),w(書き込み用に開く),a(追記用に書く),+(読み書き両用にする),b(バイナリモードで開く)



print('How to open file 2') #with open(引数列) as　変数名：

with open('data/visitor_record.txt', 'r', encoding='UTF-8')
as f:
        for line in f:
            if '東京都' in line:
                print(line.replace('¥n',''))

print('How to ')
f = open('output.txt','w',encoding='UTF=8')
for i in range(0,100):
    f.write(str(i) + '￥n')

print('7-3 データの集計とグラフ描画')
#情報可視化技術
#Step1　データ集計

pref_count_dict = {} # create empty object 
with open('data/visitor_record.txt','r', encoding='UTF-8')
as f 
    for line in f: 
        date, pref, num_adult, num_children = line.split(',')
        num_all = int(num_adult) + int(num_children)
        if pref in pref_count_dict:
            pref_count_dict[pref] += num all 
        else:
            pref_count_dict[pref] = num all 

pref_count_sorted = sorted( 
pref_count_dict.items(), 
key=lanbda x:x[1], reverse=True)

for i in pref_count_sorted:
    print(i)
