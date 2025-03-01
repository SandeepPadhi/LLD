from storage.storage import InMemoryStorage
from transaction.transaction_manager import TransactionManager
from lockmanager.lockmanager import LockManager
from model.model import Account,TransactionType,Transaction
from datetime import datetime
import random


class Bank:
    def __init__(self):
        self.storage=InMemoryStorage()
        self.lock_manager=LockManager()
        self.transaction_manager=TransactionManager(self.storage,self.lock_manager)

    
    def create_account(self,name,amount,dateTime:datetime):
        account=Account(name,amount,dateTime)
        self.storage.save_account(account)
    
    def make_transaction(self,fromAccount:Account,amount:int,transactiontype:TransactionType,to:Account=None):
        transaction=Transaction(random.randint(1,1000),fromAccount,amount,Transaction)
        self.transaction_manager.transaction_queue.put(transaction)

