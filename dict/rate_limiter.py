"""
Scenario: Implement a basic rate limiter. Given a stream of API requests, represented as timestamps and user IDs, 
determine if a user has exceeded a certain request limit within a given time window.
Example Input:
Python

requests = [
    {"timestamp": 1678886400, "user_id": "X"},
    {"timestamp": 1678886401, "user_id": "Y"},
    {"timestamp": 1678886402, "user_id": "X"},
    {"timestamp": 1678886403, "user_id": "X"},
    {"timestamp": 1678886404, "user_id": "Y"},
    {"timestamp": 1678886405, "user_id": "X"},
]
Requirements: Limit 3 requests per user within a 5-second window.
Focus: Using dictionaries to track user request counts and timestamps, implementing a sliding window.

"""

"""
1. timestamps to seconds conversation
2. 
"""
from collections import defaultdict

class RateLimiter:
    def __init__(self, limit, window):
        self.user_requests = defaultdict(list)
        self.limit = limit
        self.window = window

    def process(self, request):
        user_id = request["user_id"]
        timestamp = request["timestamp"]

        self.clean_up_old_requests(user_id, timestamp) #remove old requests.

        if len(self.user_requests[user_id]) < self.limit:
            self.user_requests[user_id].append(request)
            return True
        else:
            return False

    def clean_up_old_requests(self, user_id, current_timestamp):
        # Remove requests older than the window
        filtered_requests = [
            req
            for req in self.user_requests[user_id]
            if current_timestamp - req["timestamp"] <= self.window
        ]
        self.user_requests[user_id] = filtered_requests

def app():
    requests = [
        {"timestamp": 1678886400, "user_id": "X"},
        {"timestamp": 1678886401, "user_id": "Y"},
        {"timestamp": 1678886402, "user_id": "X"},
        {"timestamp": 1678886403, "user_id": "X"},
        {"timestamp": 1678886404, "user_id": "Y"},
        {"timestamp": 1678886405, "user_id": "X"},
        {"timestamp": 1678886410, "user_id": "X"},
    ]

    limit = 3
    window = 5
    rate_limiter = RateLimiter(limit, window)

    for request in requests:
        if rate_limiter.process(request):
            print(f"Successfully processed request: {request}")
        else:
            print(f"Rate limited for request: {request}")

if __name__ == "__main__":
    app()
            
            
            
        



