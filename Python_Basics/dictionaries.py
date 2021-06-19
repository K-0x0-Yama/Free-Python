# dictionary: キーと値の組み合わせを複数保持するデータ型
fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}

print(fruits_colors)


# 指定するprint出力 
print(fruits_colors['apple'])  # keyを指定すると、対になってる値が出力される

# dictionaryにkeyと値を追加する
fruits_colors['peach'] = 'pink'
print(fruits_colors)


# dictの中にdictを入れることもできるし、keyはint型でもOK
dict_sample = {1: 'one', 'two': 2, 'three': [1, 2, 3], 'four': {'inner': 'dict'}}
print(dict_sample)

# dict in dictの取り出しは
print(dict_sample['four']['inner'])


colors = {}
colors[1] = 'blue'
colors[0] = 'red'
colors[2] = 'green'
print(colors)
# {}のなかには入るけど、listみたいに順番があるわけでもない
# イメージは袋にどかっとはいってる感じ
# 出力は順番になってるが、それはpythonがただ順番に出力したにすぎず保持されてない



# for文を使ってループする時に使えるdictメソッド
# .keys() values()
# forでkeyを使って回したいときは .keys()
# forで値をを使って回したいときは .values()

for fruit in fruits_colors.keys():
    print(fruit)
for fruit in fruits_colors.values():
    print(fruit)
# dictのfor文でメソッド指定しないデフォならkeyが回る
for fruit in fruits_colors:
    print(fruit)


# dict系でよく使うメソッド .items
# keyとvalueをセットでタプルで回す
for x in fruits_colors.items():
    print(x)
# アンパックで受け取ってそれをfor文で回すこともできる    
for i, x in fruits_colors.items():
    print(f"{i} is {x}")
