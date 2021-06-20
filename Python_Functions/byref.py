# 参照渡し (byref) <->値渡し (byvalue)
def add_num(a, b):
    print(f"第1引数のaのID:{id(a)}")
    print(f"第2引数のbのID:{id(b)}")
    return a + b

one = 1
two = 2
print(f"oneのID:{id(one)}")
print(f"twoのID:{id(two)}")
print(add_num(one, two))

# 値をコピーして渡すのか
# オブジェクトそのままをいれているのか

# 参照渡しはメモリのアドレスだけをわたしている
# 値渡しは値をコピーしてわたしてるので  値としては別物のオブジェクトになる




# 今回渡した1はintegerでimmutableで変更できないオブジェクトで上書きできない
# 関数を呼んで、関数に渡した値は参照渡しではいり、値が足されたら新しいメモリに足された値を作成する
# そのためにIDが変わって見え参照渡しではなく値渡しと同じ挙動になるが、中身は参照渡しであること
# 関数内で渡したオブジェクトが変更されても、参照元はimmutbleで変更ができないタイプだし、値そのものを変数格納しているために
# oneは変わらず1のオブジェクトを参照し続けている
def add_one(num):
    print(f"変更前のID{id(num)}")
    num += 1
    print(f"変更後のID{id(num)}")
    return num

one = 1
print(id(one))
print(f"関数呼び出し前のone:{one}")
add_one(one)
print(f"関数呼び出し後のone:{one}")





# 今回関数に渡しのはlistでmutableな値つまり変更可能な値
# ↓の関数ではlistにappendした処理がはいっても参照元のIDは同じIで値が更新されるので
# 関数の外で定義した元々の値も変更されるということになる
# mutableな値を関数に渡すと参照渡しそのままの挙動になる

def add_fruit(fruits, fruit):
    print(f"変更前のID:{id(fruits)}")
    fruits.append(fruit)
    print(f"変更後のID:{id(fruits)}")
    return fruits


my_fruits = ['apple', 'banana', 'peach']
now_add_fruit = 'lemon'
print(f"関数呼び出し前のmy_fruits:{my_fruits}")
add_fruit(my_fruits, now_add_fruit)
print(f"関数呼び出し後のmy_fruits:{my_fruits}")





























