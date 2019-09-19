class SweetPotato:

    #属性


    def __init__(self):
        self.cookedString='生的'
        self.cookedLevel=0
        self.condiments = [] #为了能够储存多个数据,往往在开发中让一个属性是列表

    def __str__(self):
        return "地瓜 状态:%s(%d),添加的佐料有:%s"%(self.cookedString,self.cookedLevel,str(self.condiments))

    def cook(self,cooked_time):
        self.cookedLevel += cooked_time
        if self.cookedLevel >= 0 and self.cookedLevel < 3:
            self.cookedString = "生的"
        elif self.cookedLevel >= 3 and self.cookedLevel < 5:
            self.cookedString = "半生不熟"
        elif self.cookedLevel >= 5 and self.cookedLevel <8:
            self.cookedString = "熟了"
        else:
            self.cookedString = "烤糊了"
    def addCondiments(self,condiments):
        # 因为condiments这个变量指向了一个佐料,所以接下来需要将item放到append里面
        self.condiments.append(condiments)
# 创建一个地瓜对象
di_gua = SweetPotato()
print(di_gua)
# 开始开地瓜
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.addCondiments("番茄酱")
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("孜然")
print(di_gua)
di_gua.cook(1)
print(di_gua)
