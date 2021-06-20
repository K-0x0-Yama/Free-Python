# 関数の中で関数を定義(nested function)
def outer():
    def inner():
        print("This is inner function")
    inner()


outer()


# inner()  # nested functionのinner関数は外から呼ぶことができない


# nested functionはクロージャーとかデコレータを学ぶ導入てきなもの


# inner functionはouter functionの変数にアクセスできる
def outer1(outer_param):
    def inner1():
        print("This is inner function")
        print(outer_param)
    inner1()


outer1("outer arg")


# outer functionからinner functionの変数にアクセスすることはできない

# nested functionでは nonlocalを定義することでスコープをローカルのものにしないことができる
msg = "I am global"


def outer2():
    msg = "I am outer"


    def inner2():
        nonlocal msg
        msg = "I am inner"
        print("This is inner function")
        print(msg)
    inner2()
    print(msg)


outer2()
print(msg)
