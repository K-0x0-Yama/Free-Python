# is演算子:同じオブジェクトかどうかを判定する

a = 1
b = 1
c = 3
d = a
e = 2 - 1  # 1

print(id(1))
print(id(a))
print(id(b))

print(a is b)  # True
print(d is a)  # True
print(d is b)  # True

# 計算されてるオブジェクトを判定
print(a is e)  # True

# is not:is演算子を否定形で使用できる
print(a is not c)  # True

# 文字列の場合
hello = "hello"
hello2 = "h" + "e" + "l" + "l" + "o"  # "hello"
print(hello, hello2)
print(hello is hello2)  # True

#変数上書き後の挙動
hello = "konnichiwa"
print(hello is hello2)  # False

# Noneかどうかの判定によくつかう
nothing = None
print(nothing is None)
print(id(nothing))
print(id(None))
