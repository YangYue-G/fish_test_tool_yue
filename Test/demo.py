# 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
"""
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            # 判断是否有重复的数字，如果互不重复则执行下面语句
            if (x != y) and (y != z) and (z != x):
                print("%d%d%d" % (x, y, z))
"""

"""
企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成
从键盘输入当月利润I，求应发放奖金总数？
"""

a = int(input("请输入当月利润金额："))
if a <= 10000:
    print("本月奖金应发放：", a * 0.1)
elif 200000 > a > 100000:
    x = a % 100000
    print("本月奖金应发放：", (x * 0.075) + ((a - x) * 0.1))
    # print("本月奖金应发放："100000 * 0.1 + (a - 100000) * 0.075)
elif 400000 > a > 200000:
    print("本月奖金应发放：", )