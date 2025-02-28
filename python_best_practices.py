"""
Python Best Practices Reference
===============================
A comprehensive guide to Python best practices for interviews and professional development.
"""

# ===== CODE STYLE =====

# ----- PEP 8 Compliance -----
# PEP 8 is Python's style guide - following it makes code more readable

# Indentation: 4 spaces (not tabs)
def good_indentation():
    # 4 spaces for indentation
    if True:
        print("Properly indented")

# Maximum line length: 79 characters (or 88 with Black formatter)
# Long string example with proper line breaks
long_string = (
    "This is a very long string that would exceed the character limit "
    "so we break it across lines like this."
)

# Variable names: lowercase with underscores (snake_case)
user_name = "John"  # Good
userName = "John"  # Not recommended (camelCase)

# Constants: UPPERCASE with underscores
MAX_USERS = 100
PI = 3.14159

# Class names: CamelCase (PascalCase)
class UserProfile:
    pass

# Function and method names: lowercase with underscores
def calculate_total_price(price, tax):
    return price * (1 + tax)

# Imports: on separate lines and grouped
# Standard library imports first, then third-party, then local
import os
import sys
from datetime import datetime

import numpy as np
import pandas as pd

from myproject.utils import helper

# ----- Docstrings -----
# Use docstrings for modules, classes, and functions

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
    Returns:
        float: The area of the rectangle.
        
    Raises:
        ValueError: If length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative")
    return length * width

# Class docstring example
class Person:
    """
    A class representing a person.
    
    Attributes:
        name (str): The person's name.
        age (int): The person's age.
    """
    
    def __init__(self, name, age):
        """
        Initialize a Person object.
        
        Args:
            name (str): The person's name.
            age (int): The person's age.
        """
        self.name = name
        self.age = age


# ===== CODE ORGANIZATION =====

# ----- Imports -----
# Avoid wildcard imports
# Bad:
# from math import *

# Good:
from math import sqrt, pi

# Use absolute imports when possible
# from mypackage.mymodule import MyClass

# Aliasing imports for clarity or to avoid conflicts
import numpy as np
import pandas as pd

# ----- Functions -----
# Functions should do one thing only

# Bad - function does multiple things
def process_data_bad(data):
    # Clean data
    cleaned = [item.strip() for item in data if item]
    # Transform data
    transformed = [item.upper() for item in cleaned]
    # Save data
    with open("output.txt", "w") as f:
        for item in transformed:
            f.write(item + "\n")

# Good - separate functions for each task
def clean_data(data):
    return [item.strip() for item in data if item]

def transform_data(data):
    return [item.upper() for item in data]

def save_data(data, filename):
    with open(filename, "w") as f:
        for item in data:
            f.write(item + "\n")

def process_data_good(data):
    cleaned = clean_data(data)
    transformed = transform_data(cleaned)
    save_data(transformed, "output.txt")

# ----- Classes -----
# Follow the Single Responsibility Principle

class FileProcessor:
    def __init__(self, filename):
        self.filename = filename
        
    def read_data(self):
        with open(self.filename, 'r') as f:
            return f.readlines()
            
    def write_data(self, data):
        with open(self.filename, 'w') as f:
            f.writelines(data)


# ===== DATA STRUCTURES AND ALGORITHMS =====

# ----- Use Appropriate Data Structures -----

# Lists: ordered sequence of items
names = ["Alice", "Bob", "Charlie"]

# Tuples: immutable sequences
point = (10, 20)  # Coordinates

# Sets: unordered collection of unique items (fast lookups)
unique_visitors = {"Alice", "Bob", "Alice"}  # Stores only {"Alice", "Bob"}

# Dictionaries: key-value pairs (fast lookups)
user = {"name": "Alice", "age": 30, "role": "Developer"}

# Using collections module for specialized data structures
from collections import Counter, defaultdict, namedtuple

# Counter for counting occurrences
word_counts = Counter(["apple", "banana", "apple", "orange"])
# Result: Counter({'apple': 2, 'banana': 1, 'orange': 1})

# defaultdict to provide default values
group_by_age = defaultdict(list)
group_by_age[25].append("Alice")  # No KeyError if key doesn't exist

# namedtuple for readable tuples
Person = namedtuple("Person", ["name", "age"])
alice = Person("Alice", 30)
print(alice.name)  # "Alice"
print(alice.age)   # 30

# ----- Comprehensions -----
# List comprehension instead of map/filter
numbers = [1, 2, 3, 4, 5]

# Instead of:
squared_for = []
for n in numbers:
    squared_for.append(n ** 2)

# Use:
squared_comp = [n ** 2 for n in numbers]

# With filtering
even_squares = [n ** 2 for n in numbers if n % 2 == 0]

# Dictionary comprehension
square_dict = {n: n ** 2 for n in numbers}

# Set comprehension
unique_squares = {n ** 2 for n in numbers}

# ----- Generators for Memory Efficiency -----
# Generator expression (uses less memory than list comprehension)
sum_of_squares = sum(n ** 2 for n in range(1000000))

# Generator function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# ----- Use Proper Iteration -----
# Iterate directly over containers
names = ["Alice", "Bob", "Charlie"]

# Instead of:
for i in range(len(names)):
    print(names[i])

# Use:
for name in names:
    print(name)

# If you need index and value, use enumerate
for i, name in enumerate(names):
    print(f"{i}: {name}")

# For dictionaries, be specific about what you need
user = {"name": "Alice", "age": 30}

# Keys (default)
for key in user:
    print(key)

# Values
for value in user.values():
    print(value)

# Both
for key, value in user.items():
    print(f"{key}: {value}")


# ===== PERFORMANCE OPTIMIZATION =====

# ----- String Concatenation -----
# Bad (slow for many operations)
result = ""
for i in range(10000):
    result += str(i)

# Good (much faster)
parts = []
for i in range(10000):
    parts.append(str(i))
result = "".join(parts)

# ----- Use Built-in Functions and Libraries -----
# Use built-in functions when possible (they're optimized)
numbers = [1, 2, 3, 4, 5]

# Instead of:
total = 0
for num in numbers:
    total += num

# Use:
total = sum(numbers)

# ----- Avoid Global Variables -----
# Bad - using global variables
counter = 0

def increment():
    global counter
    counter += 1

# Good - pass and return values
def increment(counter):
    return counter + 1

# ----- Use Context Managers for Resources -----
# Bad - resource might not be closed if exception occurs
f = open("file.txt", "w")
f.write("Hello")
f.close()

# Good - context manager ensures resource cleanup
with open("file.txt", "w") as f:
    f.write("Hello")


# ===== ERROR HANDLING =====

# ----- Use Specific Exceptions -----
# Bad - bare except clause
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except:  # Catches ALL exceptions, including KeyboardInterrupt
    print("An error occurred")

# Good - catch specific exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:  # Fallback for other exceptions
    print(f"An error occurred: {e}")
finally:
    print("This always executes")

# ----- Custom Exceptions -----
class ValidationError(Exception):
    """Raised when input validation fails."""
    pass

def validate_age(age):
    if age < 0:
        raise ValidationError("Age cannot be negative")
    if age > 150:
        raise ValidationError("Age is unrealistically high")
    return age


# ===== FUNCTIONAL PROGRAMMING =====

# ----- Use map/filter/reduce when appropriate -----
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Map example
squared = list(map(lambda x: x ** 2, numbers))

# Filter example
even = list(filter(lambda x: x % 2 == 0, numbers))

# Reduce example
product = reduce(lambda x, y: x * y, numbers)

# ----- Use Higher-Order Functions -----
def apply_operation(operation, numbers):
    return [operation(num) for num in numbers]

def square(x):
    return x ** 2

result = apply_operation(square, numbers)

# ----- Use Decorators for Cross-Cutting Concerns -----
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Done"


# ===== TESTING AND DEBUGGING =====

# ----- Assertions for Debugging -----
def calculate_discount(price, rate):
    assert 0 <= rate <= 1, "Discount rate must be between 0 and 1"
    return price * (1 - rate)

# ----- Unit Testing -----
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')
        
    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())
        
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

# ----- Debugging with Print Statements -----
def debug_function(x, y):
    print(f"x = {x}, y = {y}")  # For debugging
    result = x * y
    print(f"result = {result}")  # For debugging
    return result

# Better approach using logging
import logging
logging.basicConfig(level=logging.DEBUG)

def better_debug(x, y):
    logging.debug(f"x = {x}, y = {y}")
    result = x * y
    logging.debug(f"result = {result}")
    return result


# ===== CONCURRENCY AND PARALLELISM =====

# ----- Threading for I/O-Bound Tasks -----
import threading
import time

def io_bound_task(name):
    print(f"Task {name} starting")
    time.sleep(1)  # Simulating I/O operation
    print(f"Task {name} completed")

threads = []
for i in range(5):
    t = threading.Thread(target=io_bound_task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# ----- Multiprocessing for CPU-Bound Tasks -----
from multiprocessing import Pool

def cpu_bound_task(n):
    return sum(i * i for i in range(n))

def multiprocessing_example():
    with Pool(4) as pool:  # 4 worker processes
        results = pool.map(cpu_bound_task, [1000000, 2000000, 3000000, 4000000])
    return results

# ----- Asyncio for Concurrent I/O Operations -----
import asyncio

async def async_task(name, delay):
    print(f"Task {name} starting")
    await asyncio.sleep(delay)  # Non-blocking sleep
    print(f"Task {name} completed")
    return name

async def main():
    tasks = [
        asyncio.create_task(async_task("A", 1)),
        asyncio.create_task(async_task("B", 2)),
        asyncio.create_task(async_task("C", 3))
    ]
    results = await asyncio.gather(*tasks)
    print(f"Results: {results}")

# asyncio.run(main())  # Uncomment to run


# ===== SECURITY BEST PRACTICES =====

# ----- Never Store Passwords in Plaintext -----
import hashlib
import os

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(32)  # 32 bytes of random data
    
    # Use a strong hashing algorithm with salt
    hash_obj = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000  # Number of iterations
    )
    
    return salt, hash_obj

# ----- Validate User Input -----
def safe_int_conversion(value):
    try:
        return int(value), None
    except ValueError as e:
        return None, str(e)

# ----- Use Parameterized Queries for Database -----
import sqlite3

def safe_query(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Bad - vulnerable to SQL injection
    # cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    
    # Good - parameterized query
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    
    result = cursor.fetchall()
    conn.close()
    return result


# ===== PACKAGING AND DISTRIBUTION =====

# ----- Project Structure -----
"""
my_project/
│
├── my_package/
│   ├── __init__.py
│   ├── module1.py
│   ├── module2.py
│   └── subpackage/
│       ├── __init__.py
│       └── module3.py
│
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
│
├── docs/
│   └── index.md
│
├── setup.py
├── README.md
├── LICENSE
└── requirements.txt
"""

# ----- Setup File Example -----
"""
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.18.0",
        "pandas>=1.0.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of my package",
    keywords="sample, package, example",
    url="https://github.com/yourusername/my_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
"""

# ----- Use Virtual Environments -----
"""
# Create a virtual environment
python -m venv myenv

# Activate it (Windows)
myenv\\Scripts\\activate

# Activate it (Unix/macOS)
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt
"""


# ===== TYPING HINTS (Python 3.5+) =====

# ----- Basic Type Annotations -----
def greet(name: str) -> str:
    return f"Hello, {name}"

# ----- Complex Types -----
from typing import List, Dict, Tuple, Optional, Union, Any, Callable

# List of integers
def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)

# Dictionary with string keys and any values
def process_data(data: Dict[str, Any]) -> None:
    for key, value in data.items():
        print(f"{key}: {value}")

# Optional parameter (can be None)
def get_user(user_id: int, cache: Optional[Dict] = None) -> Dict:
    if cache and user_id in cache:
        return cache[user_id]
    # Fetch user from database...
    return {"id": user_id, "name": "User"}

# Union type (multiple possible types)
def process_input(data: Union[str, bytes]) -> str:
    if isinstance(data, bytes):
        return data.decode('utf-8')
    return data

# Function type
def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)


# ===== PERFORMANCE PROFILING =====

# ----- Simple Timing -----
import time

def time_function(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Function took {end_time - start_time:.4f} seconds")
    return result

# ----- Using the timeit module -----
import timeit

def measure_performance():
    setup = "lst = list(range(1000))"
    
    list_comp_time = timeit.timeit(
        stmt="[x*2 for x in lst]",
        setup=setup,
        number=10000
    )
    
    map_time = timeit.timeit(
        stmt="list(map(lambda x: x*2, lst))",
        setup=setup,
        number=10000
    )
    
    print(f"List comprehension: {list_comp_time:.6f}s")
    print(f"Map function: {map_time:.6f}s")

# ----- Using cProfile -----
import cProfile

def profile_function(func, *args, **kwargs):
    return cProfile.runctx('func(*args, **kwargs)', 
                          globals(), 
                          {'func': func, 'args': args, 'kwargs': kwargs})


# ===== PYTHON DESIGN PATTERNS =====

# ----- Singleton Pattern -----
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# ----- Factory Pattern -----
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# ----- Observer Pattern -----
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    
    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)

class Observer:
    def update(self, subject, *args, **kwargs):
        pass


# ===== PYTHONIC CODE EXAMPLES =====

# ----- Swapping Values -----
a, b = 1, 2
a, b = b, a  # Swap values without temporary variable

# ----- Default Dict Values with get() -----
user_data = {"name": "Alice"}
# Instead of:
if "age" in user_data:
    age = user_data["age"]
else:
    age = 30

# Use:
age = user_data.get("age", 30)

# ----- Context Managers -----
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Acquiring resource")
    resource = {"data": "important"}
    try:
        yield resource
    finally:
        print("Releasing resource")
        resource.clear()

# ----- Unpacking -----
# List unpacking
first, *rest, last = [1, 2, 3, 4, 5]
# first = 1, rest = [2, 3, 4], last = 5

# Dictionary unpacking
def create_user(**user_info):
    # Process user info
    return user_info

user = {"name": "Alice", "age": 30}
extra_info = {"role": "Admin", "active": True}

# Combine dictionaries (Python 3.5+)
full_user = {**user, **extra_info}

# ----- One-liners -----
# Find all even numbers in a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]

# Count words in a text
text = "the quick brown fox jumps over the lazy dog"
word_count = len(text.split())

# Check if all/any elements meet a condition
all_positive = all(x > 0 for x in numbers)
any_even = any(x % 2 == 0 for x in numbers)


# ===== PYTHON 3 MODERN FEATURES =====

# ----- F-strings (Python 3.6+) -----
name = "Alice"
age = 30
# Instead of:
message = "Hello, {}. You are {} years old.".format(name, age)
# Use:
message = f"Hello, {name}. You are {age} years old."
# With expressions:
message = f"Hello, {name.upper()}. In 5 years you'll be {age + 5} years old."

# ----- Walrus Operator := (Python 3.8+) -----
# Instead of:
data = get_data()
if data:
    process(data)

# Use:
if data := get_data():
    process(data)

# ----- Dataclasses (Python 3.7+) -----
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0
    
    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

# ----- Positional-only and Keyword-only Arguments (Python 3.8+) -----
def calculate(a, b, /, *, operation="add"):
    # a, b are positional-only (before /)
    # operation is keyword-only (after *)
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    else:
        raise ValueError(f"Unknown operation: {operation}")

# Call with positional args for a, b and keyword for operation
result = calculate(1, 2, operation="multiply")

# ----- Pattern Matching (Python 3.10+) -----
def process_command(command):
    match command.split():
        case ["quit"]:
            return "Exiting program"
        case ["load", filename]:
            return f"Loading {filename}"
        case ["save", filename]:
            return f"Saving to {filename}"
        case ["search", *keywords]:
            return f"Searching for: {' '.join(keywords)}"
        case _:
            return "Unknown command"

# ===== NUMPY AND PANDAS BEST PRACTICES =====

# Vectorize operations with NumPy
import numpy as np

# Avoid loops for numerical operations
# Instead of:
def slow_distance(x1, y1, x2, y2):
    result = []
    for i in range(len(x1)):
        result.append(((x2[i] - x1[i])**2 + (y2[i] - y1[i])**2)**0.5)
    return result

# Use:
def fast_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Using Pandas efficiently
import pandas as pd

# Use vectorized string operations
df = pd.DataFrame({
    "name": ["John Smith", "Jane Doe", "Bob Johnson"]
})

# Instead of:
def extract_first_name_slow(df):
    first_names = []
    for name in df["name"]:
        first_names.append(name.split()[0])
    return first_names

# Use:
def extract_first_name_fast(df):
    return df["name"].str.split().str[0]

# Use apply when vectorization is not possible
df["full_length"] = df["name"].apply(lambda x: len(x.replace(" ", "")))


# ===== FINAL TIPS =====

# ----- Common Interview Questions -----

# 1. List vs Tuple vs Set
"""
Lists:
- Mutable, ordered collection
- Good for storing items that need to change
- Example: [1, 2, 3, 'a', 'b']

Tuples:
- Immutable, ordered collection
- Good for fixed data, faster than lists
- Example: (1, 2, 3, 'a', 'b')

Sets:
- Mutable, unordered collection of unique items
- Fast membership testing
- Example: {1, 2, 3, 'a', 'b'}
"""

# 2. GIL (Global Interpreter Lock)
"""
The GIL is a mutex that protects access to Python objects.
It prevents multiple threads from executing Python bytecode at once.
This means that threading in Python is not truly parallel for CPU-bound tasks.
For CPU-bound tasks, use multiprocessing instead of threading.
"""

# 3. Memory Management
"""
Python uses automatic memory management with garbage collection.
Objects are removed when their reference count drops to zero.
There's also a cyclic garbage collector for reference cycles.
Use context managers to ensure proper resource cleanup.
"""

# 4. Python 2 vs Python 3
"""
Key differences:
- Print is a function in Python 3: print("Hello") vs print "Hello"
- Integer division in Python 3: 3/2 == 1.5 vs 3/2 == 1 in Python 2
- Unicode strings by default in Python 3
- Exception handling syntax changes
- Many standard library reorganizations
"""

# 5. Key Modules to Know
"""
- os: Operating system interface
- sys: System-specific parameters and functions
- datetime: Date and time handling
- re: Regular expressions
- json: JSON encoding/decoding
- collections: Specialized container datatypes
- itertools: Functions for efficient iteration
- functools: Higher-order functions
- threading/multiprocessing: Concurrency
- unittest: Unit testing framework
"""

if __name__ == "__main__":
    print("This is a reference file. Import specific functions or review the code.")