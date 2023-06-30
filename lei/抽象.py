# 定义了一个抽象类
class AC:
    def cool(self):
        pass

    def hot(self):
        pass


# 继承这个抽象类，必须重写他的所有方法
class MeiDi(AC):
    def cool(self):
        print("美的空调制冷")

    def hot(self):
        print("美的空调制热")


class GeLi(AC):
    def cool(self):
        print("格力空调制冷")

    def hot(self):
        print("格力空调制热")


def my_cool(ac: AC):
    ac.cool()


meidi = MeiDi()
geli = GeLi()

my_cool(meidi)
my_cool(geli)
