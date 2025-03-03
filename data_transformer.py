"""
[
    {"user_id": "user1", "page_url": "/home", "timestamp": 1678886400},
    {"user_id": "user2", "page_url": "/products", "timestamp": 1678886460},
    {"user_id": "user1", "page_url": "/products", "timestamp": 1678886520},
    {"user_id": "user3", "page_url": "/home", "timestamp": 1678886580},
    {"user_id": "user2", "page_url": "/products", "timestamp": 1678886640},
    {"user_id": "user1", "page_url": "/home", "timestamp": 1678886700},
    {"user_id": "user1", "page_url": "/home", "timestamp": 1678886760},
    {"user_id": "user4", "timestamp": 1678886800}, #malformed data
]

"""

from collections import defaultdict
import json

input_arr=[
    {"user_id": "user1", "page_url": "/home", "timestamp": 1678886400},
    {"user_id": "user2", "page_url": "/products", "timestamp": 1678886460},
    {"user_id": "user1", "page_url": "/products", "timestamp": 1678886520},
    {"user_id": "user3", "page_url": "/home", "timestamp": 1678886580},
    {"user_id": "user2", "page_url": "/products", "timestamp": 1678886640},
    {"user_id": "user1", "page_url": "/home", "timestamp": 1678886700},
    {"user_id": "user1", "page_url": "/home", "timestamp": 1678886760},
    {"user_id": "user4", "timestamp": 1678886800}, #malformed data
]

USER_ID="user_id"
PAGE_URL="page_url"
TIMESTAMP="timestamp"

def app(input_arr):
    request_dict=dict()
    for request in input_arr:
        if USER_ID not in request:
            continue 
        user_id=request[USER_ID]

        if PAGE_URL not in request:
            continue
        page_url=request[PAGE_URL]

        if TIMESTAMP not in request:
            continue

        timestamp=request[TIMESTAMP]

        if user_id not in request_dict:
            request_dict[user_id]=defaultdict(int)
        
        request_dict[user_id][page_url]+=1
    
    json_str=json.dumps(request_dict,indent=4)
    return json_str

if __name__ == "__main__":
    ans=app(input_arr)
    print(ans)




        
    



