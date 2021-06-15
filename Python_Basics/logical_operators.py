# 論理演算子 (logical operators)
# and, or, not
a = 1
b = 1
c = 10
d = 100
print(a == b and c > d)  #　aとbは等しい且つcはdよりも多い→ False
print(a == b or c > d)  #　aとbは等しいもしくわcはdよりも多い→ True

# 年齢が10歳以上かつ身長が110cm以上なら乗れるアトラクション
age = 10
tall = 110
print(age >= 10 and tall >= 110)

# 修士号保持もしくわ5年以上の実務経験があればVisaの取得が可能
sikaku = True
keikenn = 5
print(sikaku or keikenn >= 5)
