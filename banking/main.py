import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from bank.bank import Bank
from model.model import TransactionType
from datetime import datetime


"""
Functional Requirements: 
1. Customer will talk to bank
2. Customer can deposit, withdraw or transfer money.
3. Multiple customers can interact with bank at once.
4. ACID properties has to be maintained.
5. Concurrent accesss of shared resources has to be handled.



Non functional Requirements:
1. It should be able to handle any numbers of users given the resources



Entities:
Customers -> Account -> Transactions

Transaction -> Accounts

Bank -> Account
     -> Transactions



Flow:
1. Customer will make an account in the bank
2. Customer will perform various operations in the bank . These should be thread safe
    2.1 Deposit -> In account 
    2.2 Withdraw -> From account
    2.3 Transfer -> Btw account

    Management of these systems should be part of bank.

3. Parallel transactions simulation:
    1. We will create bank and various functionalities in it
    2. We then simulate concurrency via threads.
    3. Concurrency handle will be done via locks.
        1. Accounts will have locks.
    4. How will you avoid deadlocks ?
        1





"""


def main():
    bank=Bank()
    bank.create_account("sandeep",220, datetime.now())
    bank.create_account("ajay",100, datetime.now())
    print("accounts added")
    bank.make_transaction("sandeep",10,TransactionType.DEPOSIT)
    

if __name__ == "__main__":
    main()
