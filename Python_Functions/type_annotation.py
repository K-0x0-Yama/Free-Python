# Type annotation

def add_nums(num1, num2):
    return num1 + num2


print(add_nums(1, 2))



# parameterに型の記述ができる
def add_nums_type(num1: int, num2: int) -> int:
    return num1 + num2


print(add_nums('1', '2'))  # ホバーするとhintになる情報を表示してくれる このことをtype annnotaionという
# type annnotaion以外の記述をしてもプログラムは実行できる あくまで警告はでるが 型のヒントにすぎない

# pythonは動的型付け言語なので type annnotaionを指定するのは設計思想的にはずれている
#
