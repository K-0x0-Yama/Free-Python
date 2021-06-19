age = int(input('何歳ですか？:'))
casino_age = 10
game_text = {'1': 'ルーレット', '2': 'ブラックジャック', '3': 'ポーカー'}

if age >= casino_age:
    print('どうぞお入りください')
    while True:
        choice_game = input(f'{game_text} 数字で選んでください')
        if choice_game in game_text:
            print(game_text[choice_game])
            break
        else:
            print('1-3で選んでください')
else:
    print('18歳未満は入店できません')
