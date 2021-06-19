# tuple(タプル): 変更できないリスト []ではなく()をつかう


# tupleを作ってみる
tuple_date_of_birth = (1990, 2, 3)

# tupleのデータを取り出す lists型と同じように取り出せる
print(tuple_date_of_birth[0])

# tupleは変更できなことを確認する
# tuple_date_of_birth[0] = 2000
print(tuple_date_of_birth)  # TypeErrorになる

# tupleなものをパックされているというイメージ
# tupleを変数に分配する(代入)することをアンパックという
# enumerateとかをつかったときはアンパックしていたという


# アンパックしてみよう
year, month, date = tuple_date_of_birth
print(year)
print(month)
print(date)
