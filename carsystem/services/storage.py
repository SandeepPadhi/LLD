
from threading import Lock


class Storage: 
    def __init__(self):
        self.storageLock=Lock()
        self.buyerList=[]
        self.vendorList=[]
        self.cardict={}
        self.buyerdict={}
    
    def save_car(self,car):
        if car.name not in self.cardict:
            self.cardict[car.name]=[]
        self.cardict[car.name].append(car)
    
    def get_buyer(self,name):
        return self.buyerdict[name]
        

    def get_car(self,carname,vendor_id):
        print("yes get car")
        for crn,carList in self.cardict.items():
            print("crn:{} , carList:{}".format(crn,carList))
            if carname==crn:
                for car in carList:
                    print("car name:{} , vendor_id:{} , vendor_id:{}".format(car.name, car.vendor_id,vendor_id))
                    if car.vendor_id == vendor_id: 
                        print("done bro")
                        return car

        raise ValueError("No car available with carname:{} and vendor_id:{}".format(carname,vendor_id))
    
    def register_vendor(self,vendor):
        if vendor not in self.vendorList:
            self.vendorList.append(vendor)
    
    def register_buyer(self,buyer):
        if buyer not in self.buyerList:
            self.buyerList.append(buyer)
        self.buyerdict[buyer.name]=buyer
        
