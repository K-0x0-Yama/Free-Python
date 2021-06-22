# Decorator: 関数に機能を付属する(デコレートする)
# 関数の中身を変えることなく機能を追加することができる


def greeting(func):
    def inner(*args, **kwargs):
        print("Hello!")
        func(*args, **kwargs)
        print("Nice to meet yot!")
    return inner

@greeting
def say_name(name):
    print(f"I'm {name}")


@greeting
def say_name_and_origin(name, origin):
    print(f"I'm {name}, I'm from {origin}")




# f = greeting(say_name)
say_name("Jiro")
say_name_and_origin('Taro', 'Tokyo')
# 関数say_nameに名前の前にhelloをいれて、名前の後によろしくと入れる

