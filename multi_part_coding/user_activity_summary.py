import json
from pydantic import BaseModel,ValidationError,Field,ConfigDict
from collections import defaultdict
from typing import Union,Optional,List

"""
Ref: https://gemini.google.com/app/b3b8ff0fb08bd4da?hl=en-IN

"""


input_str_v1="""
[
    {"user_id": 1, "activity_type": "login", "timestamp": 1678886400},
    {"user_id": 2, "activity_type": "post", "timestamp": 1678886500},
    {"user_id": 1, "activity_type": "post", "timestamp": 1678886600},
    {"user_id": 2, "activity_type": "comment", "timestamp": 1678886700},
    {"user_id": 1, "activity_type": "login", "timestamp": 1678886800}
]
"""

input_str_v2="""
[
    {"user_id": 1, "activity_type": "login", "timestamp": 1678886400, "device": "desktop"},
    {"user_id": 2, "activity_type": "post", "timestamp": 1678886500, "device": "mobile"},
    {"user_id": 1, "activity_type": "post", "timestamp": 1678886600},
    {"user_id": 2, "activity_type": "comment", "timestamp": 1678886700, "device": "desktop"},
    {"user_id": 1, "activity_type": "login", "timestamp": 1678886800, "device": "mobile"}
]
"""


input_str_v3="""
[
    {"user_id": 1, "activity_type": "login", "timestamp": 1678886400, "device": "desktop", "duration": 60},
    {"user_id": 2, "activity_type": "post", "timestamp": 1678886500, "device": "mobile", "duration": 120},
    {"user_id": 1, "activity_type": "post", "timestamp": 1678886600, "duration": 90},
    {"user_id": 2, "activity_type": "comment", "timestamp": 1678886700, "device": "desktop", "duration": 30},
    {"user_id": 1, "activity_type": "login", "timestamp": 1678886800, "device": "mobile", "duration": 45}
]
"""

input_str_v4="""
[
    {"user_id": 1, "activity_type": "login", "timestamp": 1678886400, "device": "desktop", "duration": 60, "region": "US", "activity_status":"success"},
    {"user_id": 2, "activity_type": "post", "timestamp": 1678886500, "device": "mobile", "duration": 120, "region": "EU", "product_id": 123, "activity_status":"success"},
    {"user_id": 1, "activity_type": "post", "timestamp": 1678886600, "duration": 90, "region": "US", "product_id": 456, "activity_status":"failed"},
    {"user_id": 2, "activity_type": "comment", "timestamp": 1678886700, "device": "desktop", "duration": 30, "region": "EU", "activity_status":"pending"},
    {"user_id": 1, "activity_type": "login", "timestamp": 1678886800, "device": "mobile", "duration": 45, "region": "Asia", "activity_status":"success"},
    {"user_id": 1, "activity_type": "purchase", "timestamp": 1678886800, "device": "mobile", "duration": 45, "region": "Asia", "product_id":123, "activity_status":"success"}
]
"""




class Activity(BaseModel):
    """
    hello
    """
    user_id:int
    activity_type:str
    timestamp:int
    device:Union[str,None]=Field(default=None)
    duration:Optional[int]=Field(default=0)
    model_config=ConfigDict(extra="forbid")
    region:Optional[str]=Field(default="")
    product_id:Optional[int]=Field(default=None)
    activity_status:Optional[str]=Field(default=None)

    def get_field_value(self, field_name):
        """
        Retrieves the value of an object's field by its name (as a string).

        Args:
            field_name: The name of the field to retrieve.

        Returns:
            The value of the field, or None if the field doesn't exist.
        """
        try:
            return getattr(self, field_name)
        except AttributeError:
            return None


def convert_dict_to_Class(dictionary,cls):
    return cls(**dictionary)

def get_input(source,input_type):
    if input_type=="string":
        return json.loads(source)
    else:
       with open(source,'r') as file:
          return json.load(file)
       
def process_data_v1(input_data:list[Activity]):
    output=defaultdict(lambda:defaultdict(int))
    for inp in input_data:
        activity_type=inp.activity_type
        user_id=inp.user_id
        output[user_id][activity_type]+=1
    return output

def process_data_v2(input_data:list[Activity]):
    output=defaultdict(lambda:defaultdict(lambda : defaultdict(int)))
    for inp in input_data:
        activity_type=inp.activity_type
        user_id=inp.user_id
        device=inp.device
        output[user_id][activity_type]["count"]+=1
        if device:
            output[user_id][activity_type][device]+=1
    return output


def process_data_v3(input_data:list[Activity]):
    output=defaultdict(lambda:defaultdict(lambda : defaultdict(int)))
    for inp in input_data:
        activity_type=inp.activity_type
        user_id=inp.user_id
        device=inp.device
        duration=inp.duration
        output[user_id][activity_type]["count"]+=1
        if device:
            output[user_id][activity_type][device]+=1
        output[user_id][activity_type]["duration"]+=duration
    return output


def process_data_v4(input_data:list[Activity]):
    output=defaultdict(lambda:defaultdict(lambda : defaultdict(int)))
    for inp in input_data:
        activity_type=inp.activity_type
        user_id=inp.user_id
        device=inp.device
        duration=inp.duration
        product_id=inp.product_id
        activity_status=inp.activity_status
        output[user_id][activity_type]["duration"]+=duration
        region=inp.region
        output[user_id][activity_type]["count"]+=1
        if device:
            output[user_id][activity_type][device]+=1
      
        if activity_status:
            if "activity_status" not in output[user_id][activity_type]:
                output[user_id][activity_type]["activity_status"]=defaultdict(int)
            output[user_id][activity_type]["activity_status"][activity_status]+=1
        if product_id:
              if "product_id" not in output[user_id][activity_type]:
                output[user_id][activity_type]["product_id"]=defaultdict(int)
              output[user_id][activity_type]["product_id"][product_id]+=1

    return output

def filter(arr:List[Activity],filter):
    return [item for item in arr if all(item.get_field_value(key)==val for key,val in filter.items())]

def convert_dictionary_to_str(d:dict):
    return json.dumps(d,indent=4)
    
def main():
    input_array=get_input(input_str_v4,"string")
    if not isinstance(input_array,list):
        print("input is not an array. Returing")
        return 
    product_array=[convert_dict_to_Class(x,Activity) for x in input_array]
    filters = {"region": "US", "activity_type": "post"}
    output=process_data_v4(filter(product_array,filters))
    print(convert_dictionary_to_str(output))
    
main()
