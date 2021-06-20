




age = 30

# gobal キーワードの後に変数名を記述するとその変数名はグローバルの変数を参照する
def print_age():
    global age
    age = 20
    print(f"I'm {age} years old")


print_age()
print(age)




# 変数名を全て大文字で記述することで定数という意味になる
CALL_COUNT = 0


def print_count():
    global CALL_COUNT
    CALL_COUNT += 1
    print(f"関数1: {CALL_COUNT}回目")


print_count()
print_count()
print_count()
print_count()
print_count()
print_count()
print_count()
print_count()
