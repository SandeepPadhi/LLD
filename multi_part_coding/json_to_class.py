import json
from pydantic import BaseModel, ValidationError, ConfigDict

class Specs(BaseModel):
    cpu: str
    ram: str
    model_config = ConfigDict(extra='forbid')

class Product(BaseModel):
    name: str
    price: float
    specs: Specs
    features: list
    model_config = ConfigDict(extra='forbid')

json_data = """
{
  "name": "Laptop",
  "price": 1200.00,
  "specs": {
    "cpu": "i7",
    "ram": "16GB",
  },
  "features": ["fast", "reliable"]
}
"""

data = json.loads(json_data)

try:
    product = Product(**data)
    print(product)
except ValidationError as e:
    print(f"Validation Error: {e}")