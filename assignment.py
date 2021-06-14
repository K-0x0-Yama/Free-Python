# 変数代入してみる
a = "Hell World"
print(a)


'''
命名規則

snake_case
文字から始まる
文字、数字 _(アンダースコアを使う)
Case sensitive(Hellとhellは別の変数)

'''

# 変数
hello = "konnichiwa"
world = "sekai"
print(hello + world)


# format
# 文字列メソッドの呼び方
print("{} {}".format(hello, world))

name = "John"
print("Hey, {}!! How are you doing?".format(name))
print(f"Hey, {name}!! How are you doing?")  # fstringを使って書き直して見る

# fstring python3.5から推奨されたものでformatに比べると内部的に速い処理をしている
print(f"{hello} {world}")


print(type(name))
print(id(name))
