import re

# Regular Expression (正規表現 通称RegEx)

# ある文字列が特定のパターンにマッチするかどうかを判定できる

email = "myemai@gmail.com"  # このemailが正しいフォーマットなのかを判定する

mathced = re.search('@\w+\.', email)
print(mathced)
if mathced:
    print(mathced)
    print('マッチしたよ')
else:
    print('Not found!')

# metacharacter
# [] []のなかのものが一文字でもマッチしてるか
print(re.search('[abc]', 'apple'))
print(re.search('[a-c]', 'apple'))
print(re.search('[0-9]', 'apple'))
print(re.search('[0-9]', 'appleflajofeaan9'))

# ^ ^は最初の文字を判定する
print(re.search('^[0-9]', '0test'))  # 最初の文字が数字かを判定している

# {n} {}の中に数字を記入すると、n回リピートという意味になる
print(re.search('^[0-9]{4}', '2021/3'))  # 最初の文字から数字が4つあるかを判定することになる
# {n,m} 最低n回、最高m回リピート
print(re.search('^[0-9]{2,4}', '2021/3'))  # 最初の文字から数字が最高4つをリピート判定
print(re.search('^[0-9]{2,4}', '21/3'))  # 最初の文字から数字が最高2つをリピート判定

# $ $は最後の文字がマッチするかを判定する
print(re.search('[0-9]{2}$', '2021/3/01'))  # 最後の2文字が数字かを判定している

# * *は左のパターンを0回以上繰り返す
print(re.search('a*b', 'aaaaaab'))

# + +は左のパターンを1回以上繰り返す
print(re.search('a+b', 'b'))
print(re.search('a+b', 'ab'))

# ? ?は左のパターンを0回か1回繰り返す
print(re.search('ab?c', 'ac'))

# | |はorの役割
print(re.search('abc|012', 'abc'))

# ()グループ
print(re.search('te(s|x)t', 'test'))


# . .は任意の1文字を表す
print(re.search('h.t', 'hot'))

# \ \はエスケープ
print(re.search('h\.t', 'h.t'))

# \w \wは[a-zA-Z0-9_]全てのアルファベット、数字およびアンダースコア
print(re.search('h\wt', 'h_t'))







# while True:
#     b_day = input('生年月日を入力してください xxxx/xx/xx')
#     mathed = re.search('^[0-9]{4}/[0-9]{2}/[0-9]{2}$', b_day)
#     if mathed:
#         print(mathed)
#         print('正しいフォーマットです')
#         break
#     else:
#         print('正しくないフォーマットです')



x_re = '^(\w|.|,-)+@(\w|.|,-)+\.[a-zA-Z]{2.3}$'
while True:
    email = input('メールアドレスを入力してください')
    mathed = re.search(x_re, email)
    if mathed:
        print(mathed)
        print('正しいフォーマットです')
        break
    else:
        print('正しくないフォーマットです')


