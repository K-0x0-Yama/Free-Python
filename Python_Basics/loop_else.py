

# for else
fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
    choice = input(f"あなたの探しているフルーツは{fruit}ですか？ y/n")
    if choice == "y":
        print("好きなフルールが見つかってよかったです")
        break
    elif choice == "n":
        print("そうですか、、、")
    else:
        print("y/nで入力してください")
else:
    print("ループが回りきったので実行されました")


# while else

count = 0
while count < 10:
    print(count)
    count += 1
else:
    print("countは10未満ではなくなりました")


balance = 1000
game_price = 200
while game_price <= balance:
    choice = input(f"1回{game_price}円ですがプレイしますか？ y/n")
    if choice == "y":
        balance -= game_price
        print(f"プレイありがとうございました。あなたの残金は{balance}円です")
    elif choice == "n":
        print("そうですか、、、またのお越しをおまちしております")
        break
    else:
        print("y/nで入力してください")
        continue
else:
    print("プレイできるお金なくなっちゃったですね。。。")

