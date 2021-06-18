# 「:」を使って、複数の要素をとってくることができる(slicing)

even = [2, 4, 6, 8, 10, 12]
# 基本は[開始:未満]
print(even[1:4])  # 1以上4未満の要素を取得する

# 開始を省略する
print(even[0:4])
print(even[:4])

# -(マイナス)をつかったslicing
print(even[3:5])
print(even[3:-1])

# 未満を省略する
print(even[0:4])
print(even[3:])

# コロンだけにすると全ての要素を取得する
print(even[:])

# 文字列に対してもslicingできる
text = "hello world"
print(text[3:])

# [開始:未満:step]
print(text[2:10:2])

# stepに-(マイナス)を記述すると逆で取得する
print(text[::-1])

print("------------------------------------------------------------------------")

# "+"演算子でリストを結合する
print([1, 2, 3] + [4, 5, 6])  # 1つのリストに結合される

# リストを変数代入して、変数同士を結合してみる
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # 変数代入から結合しても1つのリストに結合される
c = a + b
print(c)

# augmented assignmentを使って記述もできる
a += b  # a = a + b
print(a)


print("------------------------------------------------------------------------")
# join
print(" ".join(["Hi", "My", "name", "is", "john"]))
text = " ".join(["Hi", "My", "name", "is", "john"])
print(text)

text_a = "*".join(["Hi", "My", "name", "is", "john"])
print(text_a)
# split
print("Hi My name is john".split(" "))  # デフォルトが半角スペースなので指定する必要はない

filename = "samaple.py"
print(filename.split(".")[0])
print(filename.split(".")[-1])


print("------------------------------------------------------------------------")

# fruits_list = ['banana', 'apple', 'cherry', 'peach']
# print(fruits_list)

# user_fruits = input('あなたが好きなフルーツはなんですか？')
# if user_fruits in fruits_list:
#    fruits_list.remove(user_fruits)
#    print(fruits_list)
#else:
#    fruits_list.append(user_fruits)
#    print(fruits_list)
#
print("------------------------------------------------------------------------")

# forループ
#fruits_list = ['apple', 'peach', 'grapes', 'banana']

# for fruit in fruits:
#    print(f"I Love {fruit}!!")

# for char in "hello world!!":
#    print(f"char: {char}")
# ループで回すことをイテレーションするという
# イテレーションができるオブジェクトをイテラブルという
# print(fruits)
# like_fruits = input("好きなフルーツはどれ？")

# if like_fruits in fruits:
#     print(f"この中で一番すきなのは{like_fruits}")

# for i in fruits:
#    if like_fruits == i:
#        print(f'私がすきなフルーツはこれ{like_fruits}')
#    else:
#        print(f'{i}は嫌い')

#like_fruits_list = []
#not_like_fruits_list = []

#for fruits in fruits_list:
#    user_input = input(f"{fruits}は好きですか? y/n")
#    if user_input == 'y':
#        like_fruits_list.append(fruits)
#    else:
#        not_like_fruits_list.append(fruits)

#for i in like_fruits_list:
#    print(f"好きな果物は{i}でした")
#for ni in not_like_fruits_list:
#    print(f"嫌いな果物は{ni}でした")


print("------------------------------------------------------------------------")
# range(start, stop, setp)

for i in range(1, 7, 1):
    print(i)

for i in range(1, 7):
    print(i)

for i in range(7):
    print(i)

for i in range(10):
    print(i)

for i in range(2, 5):
    print(i)

for i in range(3, 14, 2):
    print(i)

# 文字列でのrange関数
for i in range(10):
    print("hello")  # この場合変数のiは使ってない
# 上記のコードでiを使ってない場合の書き方
for _ in range(10):
    print("hello")


print("------------------------------------------------------------------------")

# FizzBuzzゲーム1-50

for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)























