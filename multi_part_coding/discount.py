import json
import os

FILENAME=f"{os.getcwd()}/multi_part_coding/input.json"
FILENAME="input.json"

LOW_VALUE=100
LOW_VALUE_STR="Low-Value"
MEDIUM_LOW_VALUE=100
MEDIUM_HIGH_VALUE=500
MEDIUM_VALUE_STR="Medium-Value"
HIGH_VALUE=500
HIGH_VALUE_STR="High-Value"
COST_LIMIT=10
DISCOUNT_PERCENTAGE=10
OUTPUT_LIMIT=500

def getInputJsonData(filename):
    try:
        with open(filename,"r") as file:
            json_input=json.load(file)
            return json_input
    except FileNotFoundError:
        print(f"file :{filename} not found")
        return None
    except json.JSONDecodeError as e:
        print(f"error occured while decoding json:{e}")
        return None
    return None

def get_value_label(price):
    if price>HIGH_VALUE:
        return HIGH_VALUE_STR 
    if MEDIUM_LOW_VALUE<=price<=MEDIUM_HIGH_VALUE:
        return MEDIUM_VALUE_STR
    if price<LOW_VALUE:
        return LOW_VALUE_STR
    raise ValueError(f"label not available for price:{price}")


def processProduct(product_datas,cost_limit,discount_percentage,limit):
    """
    Task: return list of product item greater than 10. We also have to send a discount price
    """

    if not isinstance(product_datas,list):
        return None

    result=[]
    for product_data in product_datas:
        id=product_data["id"]
        name=product_data["name"]
        price=product_data.get("price",0.00)
        if not isinstance(price,float) and not isinstance(price,int):
            price=0.00
        if price>cost_limit:
            discounted_price=price*(100-discount_percentage)/100
            try:
                category=get_value_label(price)
                result_data={key:value for key,value in product_data.items()}
                result_data["discountedPrice"] = discounted_price
                result_data["category"]=category
                result.append(result_data)
                
            except ValueError as v:
                print(f"Exception occured:{v}")


    return output(result,limit,lambda x:-x["discountedPrice"],"aggregate")


def output(result,limit,sorter_func,output_type):
    if output_type == "product_list":
        return sorted(result,key=sorter_func)[:limit]
    if output_type == "aggregate":
        aggregate={}
        for item in result:
            category=item["category"]
            discount=item["discountedPrice"]
            if category not in aggregate:
                aggregate[category]={
                    "product":[],
                    "totalDiscountedPrice": 0,
                    "averageDiscountedPrice": 0,
                    "productCount": 0
                }
            aggregate[category]["product"].append(item)
            aggregate[category]["productCount"]+=1
            aggregate[category]["totalDiscountedPrice"]+=discount
            aggregate[category]["averageDiscountedPrice"]=(aggregate[category]["totalDiscountedPrice"]/ aggregate[category]["productCount"])
        return aggregate
    return None

def main():
    data=getInputJsonData(FILENAME)
    if data:
        result=processProduct(data,COST_LIMIT,DISCOUNT_PERCENTAGE,OUTPUT_LIMIT)
        if result:
            print(f"result:{json.dumps(result,indent=4)}")


if __name__ == "__main__":
    main()
    


