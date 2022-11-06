# 剪刀石头布游戏
import random


ls = ["石头", "剪刀", "布"]
player = random.choice(ls)
computer = random.choice(ls)
print("玩家出：", player)
print("电脑出：", computer)
if ((player == "石头" and computer == "剪刀")
        or (player == "剪刀" and computer == "剪刀")
        or (player == "剪刀" and computer == "石头")):
    print("玩家胜利，电脑弱爆了")
elif player == computer:
    print("平局，再来一盘")
else:
    print("电脑胜利，决战到天亮！")
