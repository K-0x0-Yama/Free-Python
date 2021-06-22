# 再帰関数 (recursive function): 関数内で自身の関数をcallする関数
# 階乗 (factorial): 3! = 3 x 2 x 1 x = 6
# n! = n * (n-1) * (n-2) * ... * 1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))


def fibonacchi(i):
    if i < 2:
        return i
    else:
        return fibonacchi(i - 2) + fibonacchi(i - 1)


print(fibonacchi(6))


# 再起じゃないfibonacchi
def fibonacchi_x(x):
    if x < 2:
        return x
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(x-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result


# print(fibonacchi_x(6))
for m in range(50):
    # print(m, fibonacchi(m))
    print(m, fibonacchi_x(m))



# 再起バージョンは処理が重いので工夫が必要になる

