
from threading import Lock
from optional import Dict,List
from ..model.model import Account
from queue import Queue

class LockManager:

    def __init__(self):
        self.account_locks:Dict[str,Lock]={}
        self.acquired_locks:Queue[str]=Queue()
    
    def acquire_locks(self,*accounts:Account):
        for account in accounts:
            self.account_locks[account.account_id].acquire()
            self.acquire_locks.append(account.account_id)
    
    def release_locks(self):
        while not self.acquired_locks.Empty():
            account=self.acquire_locks.get()
            self.account_locks[account.account_id].release()