
from ..storage.storage import InMemoryStorage
from ..transaction.transaction import TransactionManager
from ..lockmanager.lockmanager import LockManager
from ..model.model import Account,TransactionType,Transaction

class Bank:
    def __init__(self):
        self.storage=InMemoryStorage()
        self.lock_manager=LockManager()
        self.transaction_manager=TransactionManager(self.storage,self.lock_manager)

    
    def create_account(self,name):
        account=Account(name)
        self.storage.save_account(account)
    
    def make_transaction(self,fromAccount:Account,amount:int,transactiontype:TransactionType,to:Account=None):
        transaction=Transaction(fromAccount,amount,Transaction)
        self.transaction_manager.transaction_queue.add(transaction)

