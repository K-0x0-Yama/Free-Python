# whileループ

# なにか条件を設定して、その条件がTrueの間はループを回す
# whileは〜の間という意味

count = 0
while count < 10:
    print(count)
    count += 1

# breakとcontinue
# breakはwhileをぬけれる
# continewuは次のループに送れる
# for文でも使える
while True:
    age = int(input("あなたは何歳ですか？"))
    if not 0 <= age < 120:
        print("入力された値は正しくありません")
        continue
    else:
        print(f"あなたは{age}歳です")
        break

# コードの修正することをリファクタリングという

game_list_1 = "ルーレット"
game_list_2 = "ブラックジャック"
game_list_3 = "ポーカ"
all_game_list = [game_list_1, game_list_2, game_list_3]
age_line = 18

age = int(input("あなたは何歳ですか?"))
if age <= age_line:
    print(f"{age_line}歳以上対象なので、入店できません")
else:
    print("いらっしゃいませお客様")
    print("当店で遊べるゲームの一覧でございます")
    print(game_list_1, game_list_2, game_list_3)
    while True:
        plays_game = str(input("遊ぶゲームを選んでください"))
        if not plays_game in all_game_list:
            print("そのようなゲームは当店にはございません。もう一度選んでください")
            continue
        else:
            print(f"{plays_game}を遊ばれるんですね！ではこちらえ！")
            break


        
