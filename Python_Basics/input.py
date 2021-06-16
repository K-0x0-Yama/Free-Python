# input(): ユーザの入力した値(文字列)を取得する

age = int(input("私はカジノのSPです。年齢を教えて下さい"))
check_age = 20

if age >= check_age:
    print("カジノへようこそ")
    game = int(input("遊ぶゲームを選択してください 1,2,3から選べます"))
    if game == 1:
        print("ルーレット")
    elif game == 2:
        print("ブラックジャック")   
    elif game == 3:
        print("ポーカー")
else:
    print(f"あなたは{age}歳でここは20未満入店禁止です")

