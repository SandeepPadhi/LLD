from dataclasses import dataclass
from datatime import datetime
from typing import Optional
from enum import Enum

class TransactionType(Enum): 
    DEPOSIT:"deposit"
    WITHDRAW:"withdraw" 
    TRANSFER:"transfer"

class TransactionStatus(Enum):
    PENDING:"pending"
    COMPLETED:"completed"
    FAILED:"failed"

@dataclass
class Account:
    account_id:str 
    balance:int 
    created_at:datatime 

@dataclass
class Transaction: 
    transaction_id:str  
    transactionType
    account_id: 
    amount:int   
    receiptent_account_id:Optiona[str]=None
