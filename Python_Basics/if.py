# if文

age = 19
age_alcohol = 20

if age >= age_alcohol:
    print("You can derink beer!")
else:
    print("You are too young to drink beer")

age_drive = 18
if age >= age_alcohol:
    print("You can drink beer")
elif age < age_drive:
    print("You cannot even drive!")
else:
    print("drive only")


balance = 100000
withdraw = 100000000
max_withdraw = 1000000

if balance >= withdraw:
    print(balance - withdraw)
elif max_withdraw < withdraw:
    print("引き出し上限金額です")
else:
    print("引き出せません")

