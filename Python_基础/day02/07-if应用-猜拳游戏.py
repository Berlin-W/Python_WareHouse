"""
需求：
① 从控制台输⼊要出的拳 —— ⽯头（1）／剪⼑（2）／布（3）
② 电脑 随机 出拳 —— 先假定电脑只会出⽯头，完成整体代码功能
③ ⽐较胜负
"""
user_input = int(input("请输入要出的拳-⽯头（1）／剪⼑（2）／布（3）："))
computer = 1
if user_input == computer:
    print("心有灵犀，再来一局")
elif (user_input == 2 and computer == 1) or (user_input == 1 and computer == 3) or (user_input == 2 and computer == 1):
    print("很遗憾，您输了！")
else:
    print("恭喜您，获得胜利！")



