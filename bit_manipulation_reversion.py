def is_odd(n):
    return n & 1 != 0

def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

def set_bit(n, k):
    return n | (1 << k)

def clear_bit(n, k):
    return n & ~(1 << k)

def toggle_bit(n, k):
    return n ^ (1 << k)

def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

def next_power_of_2(n):
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n += 1
    return n

def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b

def generate_subsets(nums):
    n = len(nums)
    subsets = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(nums[j])
        subsets.append(subset)
    return subsets

def is_ith_bit_set(number, i):
    mask = 1 << i
    return (number & mask) != 0

def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

def find_two_single_numbers(nums):
    xor_all = 0
    for num in nums:
        xor_all ^= num
    rightmost_set_bit = xor_all & -xor_all
    num1 = 0
    num2 = 0
    for num in nums:
        if num & rightmost_set_bit:
            num1 ^= num
        else:
            num2 ^= num
    return num1, num2

def binary_palindrome(number):
    binary_string = bin(number)[2:]
    return binary_string == binary_string[::-1]

# Setting and Clearing bits
def set_bit_function(number, bit_position):
    mask = 1 << bit_position
    return number | mask

def clear_bit_function(number, bit_position):
    mask = 1 << bit_position
    negated_mask = ~mask
    return number & negated_mask

# Example usage
print("Is 5 odd?", is_odd(5))
print("Is 8 a power of 2?", is_power_of_2(8))
print("Set bit 1 in 5:", bin(set_bit(5, 1)))
print("Count set bits in 7:", count_set_bits(7))
print("Next power of 2 for 10:", next_power_of_2(10))
print("Swapping 5 and 10:", swap(5, 10))
print("Subsets of [1, 2, 3]:", generate_subsets([1, 2, 3]))
print("Is the 1st bit set in 10?", is_ith_bit_set(10, 1))
print("Single number in [2, 2, 1]:", find_single_number([2, 2, 1]))
print("Two single numbers in [1, 2, 1, 3, 2, 5]:", find_two_single_numbers([1, 2, 1, 3, 2, 5]))
print("Is binary of 9 a palindrome?", binary_palindrome(9))
print("Set 2nd bit of 5:", bin(set_bit_function(5, 2)))
print("Clear 1st bit of 7:", bin(clear_bit_function(7, 1)))
print("Clear sign bit of -5:", bin(clear_bit_function(-5, 7)))

def print_bits(n):
    """Prints the bits of a 32-bit integer."""
    for i in range(32):
        if (n >> i) & 1:
            print(f"Bit {i}: 1")
        else:
            print(f"Bit {i}: 0")

print_bits(10)  # Example: 1010