from random import randint
a = randint(1, 10)
b = input("请输入一个1到10的数字：")
for i in range(10):
    if b == a:
        print "真聪明，猜对了"
        break
    else:
        b = input("再猜一次：")