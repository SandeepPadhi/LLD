from lockmanager.lockmanager import LockManager 
from storage.storage import InMemoryStorage
from model.model import Transaction,Account,TransactionType,TransactionStatus
from queue import Queue
import threading 



class TransactionManager: 

    def __init__(self,storage:InMemoryStorage,lock_manager:LockManager):
        self.storage=storage 
        self.lock_manager=lock_manager
        self.transaction_queue:Queue[Transaction]=Queue()
        self._process_transactions()

    def _process_transactions(self):
        def process_transaction(self): 
            while True: 
                print("yeahjhjkhh")
                transaction=self.transaction_queue.get()
                if transaction.transaction__type == TransactionType.TRANSFER:
                    self.process_transfer_transaction(transaction)
                else: 
                    self.process_single_account_transaction(transaction)
        
        thread=threading.Thread(target=process_transaction,args=(self),daemon=True)
        thread.start()

    def save_transaction(self,transaction:Transaction):
        self.storage.save_transaction(transaction)
    
    def process_transfer_transaction(self,transaction:Transaction):
        sender_account=self.storage.get_account(transaction.account_id)
        recepient_account=self.storage.get_account(transaction.recepient_account_id)

        self.lock_manager.acquire_locks(sender_account,recepient_account)

        sender_account.balance-=transaction.amount 
        recepient_account.balance+=transaction.amount 

        self.storage.save_account(sender_account)
        self.storage.save_account(recepient_account)
        self.lock_manager.release_locks()


    def process_single_account_transaction(self,transaction:Transaction):
        self.lock_manager.acquire_locks(transaction.account_id)
        account=self.storage.get_account(transaction.account_id)
        account+=transaction.amount 
    
    
    
    
