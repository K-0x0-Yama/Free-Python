fruits = ['apple', 'peach', 'grapes', 'banana']

# まずは普通に出力
for fruit in fruits:
    print(fruit)

# enumerateをつかってみる
for idx, fruit in enumerate(fruits):
    print(idx)
    print(fruit)


# 変数xにはタプル型でindex番号とリストの値が出力される
for x in enumerate(fruits):
    print(x)
