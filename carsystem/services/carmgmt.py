from threading import Lock
from models import Vendor , Buyer


class CarMgmt:
    def __init__(self,storage):
        self.storage=storage 
        self.carlock=Lock()
        self.vendorlock=Lock()
        self.buyerlock=Lock()
    
    def register_car(self,car):
        with self.carlock:
            self.storage.save_car(car)

    def register_vendor(self,vendorName,id):
        with self.vendorlock:
            v=Vendor(vendorName,id)
            self.storage.register_vendor(v)
    
    def buy_car(self,carname,vendorname,buyername):
        with self.carlock:
            try:
                car=self.storage.get_car(carname,vendorname)
                print("car:{}".format(car))
                if car.available_units>0:
                    car.available_units-=1 
                    print("buyername:{}".format(vendorname))
                    buyer=self.storage.get_buyer(buyername)
                    self.storage.save_car(car)
                    buyer.add_car(car.name)
            except Exception as e:
                print("unable to buy car. Exception:{}".format(e))

    def register_buyer(self,buyername):
        with self.buyerlock:
            buyer=Buyer(buyername)
            self.storage.register_buyer(buyer)
    
    
    

