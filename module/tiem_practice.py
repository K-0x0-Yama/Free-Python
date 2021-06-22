from functools import lru_cache  # キャッシュを利用するmoduelを導入 デコレートして機能を追加する
import time

# .time()1970/1/1秒数が表示される(Unix時間)
print(time.time())

# 秒数を分数に→ 時間に→ 日数に→ 年数に
print(time.time()/(60*60*24*365))


@lru_cache
def fib(n):
    print(f"fibonacci with {n} is runnig....")  # fib関数が実行されたら出力する
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)



# .timeを使って実行速度を測定することができる
before = time.time()
print(fib(30))
after = time.time()
print(f"recursive fibonacci took {after - before:.2f} sec.")  # beforeの後ろに:.2fと入力することで少数第2までを表示するとできる


# .ctime()今のローカル時間を文字列で返す
print(time.ctime())
# .localtime() 構造化データで返す
localtime = time.localtime()
print(localtime)
print(localtime.tm_year)


# fstringの記述方法
print(f"今の時間は{localtime.tm_year}年{localtime.tm_mon}月{localtime.tm_mday}日{localtime.tm_hour}時{localtime.tm_min}分です")
print("今の時間は{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分です".format(localtime)) # formatをつかって簡略化

# .sleep(secs) secs秒だけプログラムが待機する
# sec = 10
# print(f"{sec}秒まってください")
# time.sleep(sec)
# print(f"{sec}秒経ちました")


# 関数の実行速度(sec)を測るtimerデコレータをつくる

def func_timer(func):
    def inner_func_timer(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"{func.__name__} took {after - before:.2f} sec")
    return inner_func_timer


@func_timer
def lazy_func(sec):
    print(f"I'm working so hard ...")
    time.sleep(sec)
    print(f"I'm finally done!!")


lazy_func(3)

