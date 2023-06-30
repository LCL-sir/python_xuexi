# 面向对象过程中 私有成员变量和 私有成员方法的 访问
# 只要成员变量 与 成员方法前面有 __  就表示私有
# 成员变量 与 成员方法 只在当前的函数中才能使用
class Shouji:
    __dianya = 3.5

    def __zhuanzhang(self):
        print("转账成功")

    def on5G(self):
        if self.__dianya > 3:
            print("电压大于3V，可以开启5G")
        else:
            print("电压小于3V，不能开启5G")

    def onZhuan(self):
        self.__zhuanzhang()


shouji = Shouji()
shouji.on5G()
shouji.onZhuan()
