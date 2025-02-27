

class Buyer:
    def __init__(self,name):
        self.name=name 
        self.carList=[]
    
    def add_car(self,carname):
        self.carList.append(carname)
    
    def getcarlist(self):
        return self.carList
        