class fu:
    fuData = "父"

    def fuFun(self):
        print("这是父类方法")


class Zi(fu):
    def ziFun(self):
        print(self.fuData)


zi = Zi()

print(zi.fuData)
zi.fuFun()


# 多继承


# 复写
class phone:
    xh = "HW",

    def On5G(self):
        print("打开5G")


class myPhone(phone):
    xh = "iphone"

    def On5G(self):
        print("这是增强信号")

        # 子类调用父类
        super().On5G()


shiyong = myPhone()
print(shiyong.xh)
shiyong.On5G()
