from ..model.model import Account,Transaction
from optional import List,Dict
from threading import Lock

class InMemoryStorage: 
    def __init__(self):
        self._accounts:Dict[str,Account] = {}
        self._transactions:Dict[str,Transaction] = {}
        self._accountLock=Lock()
        self._transactionLock=Lock()
    
    def save_account(self,account:Account):
        with self._accountLock.acquire():
            self._accounts[account.account_id]=account 
        
    def get_account(self,account_id:str):
        with self._accountLock.acquire():
            return self._accounts[account_id]
    
    def save_account(self,account:Account):
        with self._accountLock.acquire():
            return self._accounts[account.account_id]=account 
    
    def save_transactions(self,transaction:Transaction):
        with self._transactionLock.acquire():
            self._transactions[transaction.transaction_id]=transaction 
    
    def update_transactions(self,transaction:Transaction):
        with self._transactionLock.acquire():
            self._transactions[transaction.transaction_id]=transaction 
    
    def get_transaction(self,transaction_id:str):
        with self._transactionsLock.acquire():
            return self._transaction[transaction_id]
    
