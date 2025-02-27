
import unittest
from services import Storage , CarMgmt
from models import Car

class TestCarMgmt(unittest.TestCase):
    def setUp(self):
        self.storage=Storage()
        car=Car("nano","1","100","1",100)
        self.carmgmt=CarMgmt(self.storage)
        self.carmgmt.register_buyer("sandeep")
        self.carmgmt.register_car(car)
        self.carmgmt.register_vendor("maruti","1")
        self.carmgmt.buy_car("nano","1","sandeep")
    
    def test_available_units(self):
        carg=self.storage.get_car("nano","1")
        assert carg.available_units == 99
        self.assertEqual(carg.available_units,99,"available units does not match")