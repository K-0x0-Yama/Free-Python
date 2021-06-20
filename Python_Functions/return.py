# return文を使わない関数定義
def print_dict(input_dict):
    for k, v in input_dict.items():
        print(f"key: {k}, value: {v}")


a = {"one": 1, "two": 2}
print(a)
print_dict(a)

# returnを使わに関数は何も返してないわけじゃない
# Noneを返している return Noneと記述していると同じこと


# returnで複数返す場合は,で区切る


def get_first_last_word(text):
    words = text.split()
    return words[0], words[-1]


text = "Hello, My name is  Mike"
firts, last = get_first_last_word(text)
print(f"firts word is {firts}, last word is {last}")


# 関数の設定をいじる
# replaceを使ってテキストを置き換える ("置き換えたい文字", "置き換えた後の文字")
def get_first_last_word_1(text):
    text = text.replace(",", "")
    words = text.split()
    return words[0], words[-1]


text = "Hello, My name is  Mike"
firts, last = get_first_last_word_1(text)
print(f"firts word is {firts}, last word is {last}")

