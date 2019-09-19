class Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.contain_item = []

    def __str__(self):
        return "房子的总面积是:%d平米,可用面积是:%d平米,户型是:%s,地址是:%s,当前房子里有:%s"%(self.area,self.left_area,self.info,self.addr,str(self.contain_item))

    def add_item(self,item):
        self.left_area -= item.get_area()
        self.contain_item.append(item.get_name())

class Bed:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area
    def __str__(self):
        return "%s占用的面积是:%d"%(self.name,self.area)

    def get_area(self):
        return self.area

    def get_name(self):
        return self.name
    
fangzi = Home(130,"三室一厅", "杭州市 江干区 下沙 高沙")

bed1 = Bed("席梦思",4)
bed2 = Bed("水星家纺",5)
fangzi.add_item(bed1)
fangzi.add_item(bed2)
print(fangzi)