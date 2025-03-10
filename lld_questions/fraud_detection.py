import random 
import time 
import unittest

class FraudDetection:
    def __init__(self):
        self.rules=[
            lambda transaction: transaction["amount"]>1000,
            lambda transaction:transaction["location"]=="unknown place",
            lambda transaction:transaction["device"]=="unknown device"
        ]
    
    def detech_fraud(self,transaction):
        return any(rule(transaction) for rule in self.rules)


def simulate_transaction():
    amount=random.randint(10,2000)
    location=random.choice(["work","home","unknown place"])
    device=random.choice(["mobile","desktop","unknown device"])

    return {"amount":amount,"location":location,"device":device}


class TestFraudDetection(unittest.TestCase):
    def setUp(self):
        self.fraud_detector=FraudDetection()

    def testfraud(self):
        for i in range(10):
            transaction=simulate_transaction()
            if self.fraud_detector.detech_fraud(transaction):
                print(f"for transaction:{transaction} is Fraud")
            else:
                print(f"for transaction :{transaction} is not fraud")
        
if __name__ == "__main__":
    unittest.main()