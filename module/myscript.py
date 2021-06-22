# import mymodule
# import package.subpackages.subpackages
# 長いがこの↑のパスをつかって呼び出す必要があるので
# fromとmodule名で関数や変数をimportしていく

# アスタリスクで全部importするが、推奨されてない、何がimportされてるかわからない
# from mymodule import *  # *のものは基本的にはimportできるか_がついてるものはできない

# moduleに名前をつけ直すことができる
# import mymodule as mm

# from mymodule import myfunc, myvariable, anotherfunc

# myfunc()
# anotherfunc()
# print(myvariable)
# # print(mymodule.myvariable)






# moduleをimportするときはカンマでくぎって1行に複数記述もできるが、importは一対一で記述する
# import文はファイルの1番上に記述する
# 書く順番は 標準ライブラリ, サードパーティのライブラリ、 自分たちのライブラリ、ローカルのライブラリ の順番で記述し、それぞれ1行あける
# そしてアルファベット順で記述すること


# sysモジュールとはpythonのbuilt in module
import sys
# pathを確認できる
print(sys.path)
sys.path.append("/Users/zen/Desktop/FreePython/Python_Functions")

# 違うフォルダのファイルを読みこんでみる
import docstring

print(docstring.multipy(3, 4))
















