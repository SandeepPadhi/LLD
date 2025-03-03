"""
Alright, let's craft a problem that effectively utilizes heaps and dictionaries, suitable for a Stripe-level interview, focusing on a practical scenario with algorithmic complexity.

Question:

"You are building a system to monitor and analyze real-time stock prices. 
You receive a stream of stock price updates,
 where each update is represented as a tuple: (timestamp, stock_symbol, price).

Your task is to implement a function that maintains a running window of the K most recent stock price updates for each stock symbol and provides the following functionalities:

update(timestamp, stock_symbol, price): Adds a new stock price update to the system.
get_top_k(stock_symbol): Returns a list of the K most recent stock prices for the given stock_symbol, sorted in descending order of timestamps. If fewer than K updates are available, return all available updates.
Your solution should be efficient in terms of both time and space complexity.
"""

from dataclasses import dataclass
import heapq
from collections import defaultdict


@dataclass
class Request:
    timestamp: int  # Specify the type as int
    stock_symbol: str # Specify the type as string
    price: float # Specify the type as float

class StockPriceSimulator:
    def __init__(self,k_top):
        self.k_top=k_top 
        self.stock_heap=defaultdict(list)
    
    def update(self,request):
        tpl=(request.timestamp,request.price)
        while len(self.stock_heap[request.stock_symbol])>=self.k_top:
            heapq.heappop(self.stock_heap[request.stock_symbol])                        
        heapq.heappush(self.stock_heap[request.stock_symbol],(request.timestamp,request.price))

    def get_top_k(self,stock_symbol):
        sorted_stock=sorted(tp  for tp in self.stock_heap[stock_symbol])
        sorted_stock.reverse()
        lt=[ tp[1] for tp in sorted_stock]
        return lt


def app():
    K=2
    system=StockPriceSimulator(K)
    system.update(Request(1, "AAPL", 150.0))
    system.update(Request(2, "GOOG", 2700.0))
    system.update(Request(3, "AAPL", 151.0))
    system.update(Request(4, "GOOG", 2705.0))
    system.update(Request(5, "AAPL", 152.0))

    print(system.get_top_k("AAPL"))  # Output: [(5, 152.0), (3, 151.0)]
    print(system.get_top_k("GOOG"))  # Output: [(4, 2705.0), (2, 2700.0)]
    print(system.get_top_k("AMZN")) # Output: []


if __name__ == "__main__":
    app()
        
