class Pople:
    name: None
    age: None

    # 内部的使用self
    def say(self):
        print(f"大家好，我的名字是:{self.name}")

    # 外部传入的直接用形参接受
    def old(self, ai):
        print(f"爱好是:{ai}")


pople = Pople()
pople.name = "龙右"
pople.age = 18
pople.say()
pople.old("唱跳rap")
