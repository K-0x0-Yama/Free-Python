# 関数の中で変数を定義することができる
# その変数をローカル変数と呼んだりする
def print_name_local():
    first_name = 'Taro'
    last_name = 'Yamamda'
    print(f"I'm {first_name} {last_name}")


print_name_local()
# print(first_name) # ローカル変数は関数の外からは呼ぶことができない

# グローバル変数(モジュール変数)ともいう
age = 30


def print_age():
    age = 20
    print(f"I'm {age} years old")


print_age()
print(age)


# ローカル変数が定義されなかったらどうなるか
def print_g_age():
    print(f"I'm {age} years old")


print_g_age()  # グローバル変数を取得する
