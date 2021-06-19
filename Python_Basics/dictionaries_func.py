fruits_color = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}

# dictの中身を普通に取得する
print(fruits_color['apple'])

'''
dictの中身を取り出そうとしたときもし
指定したものがない場合pythonはエラーを返してしまう
それを防ぐためにif文をつかってFaleseの処理を書いてもいいがながくなる
'''
# dictのfalse処理を書く
if 'peach' in fruits_color:
    print(fruits_color['peach'])
else:
    print('the key is not found')


# .get()
fruit = input('フルーツの名前を指定してください')
print(fruits_color.get(fruit, 'Nothing'))

# .update()
fruits_color2 = {'peach': 'pink', 'kiwi': 'grenn'}
fruits_color.update(fruits_color2)
print(fruits_color)

