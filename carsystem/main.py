from models import Car
from services import Storage,CarMgmt
import sys

# import os 
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    car=Car("nano","1","100","1",100)
    storage=Storage()
    carmgmt=CarMgmt(storage)
    carmgmt.register_buyer("sandeep")
    carmgmt.register_car(car)
    carmgmt.register_vendor("maruti","1")
    carmgmt.buy_car("nano","1","sandeep")
    print("done")
    carg=storage.get_car("nano","1")
    assert carg.available_units == 99

    print("car abailable:{}".format(carg.available_units))



if __name__ == "__main__":
    main()