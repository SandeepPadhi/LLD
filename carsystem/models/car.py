

class Car:
    def __init__(self,carname,car_id,price,vendor_id,available_units):
        self.name=carname 
        self.car_id=car_id 
        self.price=price 
        self.vendor_id=vendor_id 
        self.available_units=available_units 
    
    def sell(self):
        self.available_units-=1
    
