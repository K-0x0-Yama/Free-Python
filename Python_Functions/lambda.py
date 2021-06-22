# lambda関数 (無名関数)
# ちょっとした関数を作るときにつかったりする

def square(x):
    return x * x

lambda x: x * x













# この関数をlambda関数化する
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power

third_power = power(3)
print(third_power(2))
# ↓lambda化
def power1(exponent):
    return lambda base: base ** exponent


five_power = power1(5)
print(five_power(3))


# 引数にlambdaを使う

numbers = [6, 2, 5, 43, 5, 36, 67, 2]


# def filterfunc(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True

filtered_num = filter(lambda num: num % 2, numbers)
print(list(filtered_num))

