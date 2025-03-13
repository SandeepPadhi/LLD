import json 
from pydantic import BaseModel,ConfigDict,ValidationError,Field
from typing import Union
FILENAME="/Users/sandeeppadhi/Documents/interview_prep/LLD/multi_part_coding/input.json"

class Product(BaseModel):
    """
    Product class is a holder for product
    """
    id:int
    name:str
    price:float
    discount_price: Union[int,None] = Field(default=0)
    model_config=ConfigDict(extra="forbid")


def get_data(filename):
    """
    Product class is a holder for product
    """
    try:
        with open(filename,'r') as file:
            return json.load(file)
    except json.JSONDecodeError as j:
        print(f" exception:{j}")
        return None
    except Exception as e:
         print(f" exception:{e}")
         return None
    

def main():
    data=get_data(FILENAME)
    products=[Product(**x) for x in data]
    print(products)
main()
