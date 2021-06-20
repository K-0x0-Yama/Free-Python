def func(first, second, third):  # 指定しないparameterのことをポジショナるパラメーターという
    print(f"firts: {first}, second: {second}, third: {third}")

# 引数のことをparameter
# 引数にわたす値をargumentという

func("1", "2", "3")

# parameterの順番どおりにargumentを入れたくないばあいは
# キーワードを指定して入力することができる

func("1", third="3", second="2")



# デフォルト引数を指定することができる
# キーワード引数は位置引数の後に記述する必要がある
# キーワード引数以外のパラメーターを位置引数という↑で記述(ポジショナるパラメータ)
def func_1(first, second, third="3"):  # デフォルトで定義するparameterのことをキーワードパラメーターという
    print(f"firts: {first}, second: {second}, third: {third}")


func_1("1", "2")
# argumentをデフォルト引数の部分に入力すると、argumentが優先される
func_1("1", "2", "33")
