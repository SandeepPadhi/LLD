"""
Transaction Aggregation:

Scenario: You have a log of financial transactions, each represented as a dictionary with keys like user_id, amount, and currency. Write a function that aggregates the total amount spent by each user for each currency.
Example Input:

Python:

transactions = [
    {"user_id": "A", "amount": 100, "currency": "USD"},
    {"user_id": "B", "amount": 50, "currency": "EUR"},
    {"user_id": "A", "amount": 75, "currency": "USD"},
    {"user_id": "B", "amount": 20, "currency": "USD"},
    {"user_id": "A", "amount": 30, "currency": "EUR"},
]
Expected Output:
Python

{
    "A": {"USD": 175, "EUR": 30},
    "B": {"EUR": 50, "USD": 20},
}
Focus: Efficiently grouping and aggregating data, handling nested dictionaries.


"""

from collections import defaultdict
import json

transactions = [
    {"user_id": "A", "amount": 100, "currency": "USD"},
    {"user_id": "B", "amount": 50, "currency": "EUR"},
    {"user_id": "A", "amount": 75, "currency": "USD"},
    {"user_id": "B", "amount": 20, "currency": "USD"},
    {"user_id": "A", "amount": 30, "currency": "EUR"},
]

currency_list=["USD","EUR"]


spend_amount=dict()
for transaction in transactions:
    user_id=transaction["user_id"]
    amount=transaction["amount"]
    currency=transaction["currency"]
    if user_id not in spend_amount:
        spend_amount[user_id]={cur:0 for cur in currency_list}
    
    spend_amount[user_id][currency]+=amount


json_string = json.dumps(spend_amount,indent=4)
print(json_string)
