# Closure: クロージャ

# 関数(function)もオブジェクト
def computer_square(num):
    return num * num


print(computer_square)
# 関数もオブジェクトということは変数に代入ができる
f = computer_square
print(type(f))

# 関数を変数に代入できることでその変数で関数よ呼ぶことができる
print(f(10))

# listに関数を格納することもできる
function_list = ['1', 1, True, f]
print(function_list[-1](10))


# 関数も引数として渡せる
def execute_func(func, param):
    return func(param)


print(execute_func(f, 10))


# 関数をretrunする
def return_func():

    def inner_func():
        print("This is an inner function")
    return inner_func


x = return_func()
print(x)
x()


# Closure: 状態をキープした関数を作ることができる
# 状態が静的なClosure
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power

power_four = power(4)
print(power_four(3))


# 状態が動的なClosere
def average():
    nums = []


    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average


average_nums = average()
print(average_nums(5))
print(average_nums(15))
print(average_nums(4))
print(average_nums(10))
print(average_nums(12))
