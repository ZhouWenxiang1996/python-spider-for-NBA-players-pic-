
class PlayerMsg:
    def __init__(self,name,English_name,pos,height,weight,birth,city):
        self.name = name
        self.English_name = English_name
        self.pos = pos
        self.height = height
        self.weight = weight
        self.birth = birth
        self.city = city
        # self.high_school = high_school
        # self.university = university
        # self.no = no
        # self.draft = draft
        # self.money = money
    def __init__(self):
        pass
    def __init__(self,name,list1):
        self.name = name
        self.English_name = list1[0]
        self.pos = list1[1]
        self.height = list1[2]
        self.weight = list1[3]
        self.birth = list1[4]
        self.city = list1[5]
    def  toString(self):
        print(self.name)
        print(self.English_name)
        print(self.pos)
        print(self.height)
        print(self.weight)
        print(self.birth)
        print(self.city)



