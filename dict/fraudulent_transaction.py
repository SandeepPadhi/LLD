"""
Detecting Fraudulent Transactions:

Scenario: You have a list of transactions, each with an amount. 
Identify transactions that are significantly larger than the median of recent transactions 
(e.g., within the last 10 transactions).
Example Input:
Python

transactions = [10, 20, 30, 100, 15, 25, 40, 500, 22, 33, 1000]
Requirements: Define "significantly larger" as more than 3 times the median.
Focus: Using lists as a sliding window, calculating medians, and detecting outliers.


"""

