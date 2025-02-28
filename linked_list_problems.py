"""
Python Linked List Interview Questions Reference
-----------------------------------------------
This file contains common linked list problems that frequently appear in technical interviews,
along with their Python implementations.
"""

# Basic Node class for Singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Node class for Doubly Linked List
class DoublyListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

# Helper function to create a linked list from a list
def create_linked_list(elements):
    dummy = ListNode(0)
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return "->".join(values)

# -----------------------------------------------------------------------------
# 1. Reverse a Linked List
# -----------------------------------------------------------------------------
def reverse_linked_list(head):
    """
    Reverses a singly linked list.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev forward
        current = next_temp       # Move current forward
    
    return prev  # New head is the previous tail

# Test reverse_linked_list
head = create_linked_list([1, 2, 3, 4, 5])
print("Original list:", print_linked_list(head))
reversed_head = reverse_linked_list(head)
print("Reversed list:", print_linked_list(reversed_head))
print()

# -----------------------------------------------------------------------------
# 2. Detect Cycle in a Linked List
# -----------------------------------------------------------------------------
def has_cycle(head):
    """
    Determines if there is a cycle in the linked list.
    Uses Floyd's Tortoise and Hare algorithm.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    # Fast pointer moves twice as fast as slow pointer
    while fast and fast.next:
        slow = slow.next       # Move slow by 1
        fast = fast.next.next  # Move fast by 2
        
        # If they meet, there's a cycle
        if slow == fast:
            return True
    
    # If fast reaches the end, there's no cycle
    return False

# Create a list with a cycle for testing
cyclic_head = create_linked_list([1, 2, 3, 4, 5])
# Create a cycle: 1->2->3->4->5->3...
current = cyclic_head
while current.next:
    current = current.next
cycle_point = cyclic_head.next.next  # Points to 3
current.next = cycle_point  # 5 points back to 3

print("List has cycle:", has_cycle(cyclic_head))
print("Normal list has cycle:", has_cycle(create_linked_list([1, 2, 3])))
print()

# -----------------------------------------------------------------------------
# 3. Find the Middle of a Linked List
# -----------------------------------------------------------------------------
def middle_node(head):
    """
    Find the middle node of a linked list.
    If there are two middle nodes, return the second middle node.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return head
    
    slow = head
    fast = head
    
    # When fast reaches the end, slow will be at the middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# Test middle_node
head = create_linked_list([1, 2, 3, 4, 5])
middle = middle_node(head)
print("Middle of [1,2,3,4,5]:", middle.val)

head = create_linked_list([1, 2, 3, 4, 5, 6])
middle = middle_node(head)
print("Middle of [1,2,3,4,5,6]:", middle.val)
print()

# -----------------------------------------------------------------------------
# 4. Merge Two Sorted Linked Lists
# -----------------------------------------------------------------------------
def merge_two_lists(l1, l2):
    """
    Merges two sorted linked lists into one sorted list.
    
    Time Complexity: O(n + m)
    Space Complexity: O(1)
    """
    # Dummy node to simplify code
    dummy = ListNode(0)
    tail = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    # Attach remaining nodes
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    
    return dummy.next

# Test merge_two_lists
l1 = create_linked_list([1, 3, 5])
l2 = create_linked_list([2, 4, 6])
merged = merge_two_lists(l1, l2)
print("Merged lists:", print_linked_list(merged))
print()

# -----------------------------------------------------------------------------
# 5. Remove Nth Node From End of List
# -----------------------------------------------------------------------------
def remove_nth_from_end(head, n):
    """
    Remove the nth node from the end of the list and return the head.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head
    
    # Use two pointers - fast and slow
    fast = dummy
    slow = dummy
    
    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        if not fast:
            break
        fast = fast.next
    
    # Move both pointers until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next
    
    # Remove the nth node
    slow.next = slow.next.next
    
    return dummy.next

# Test remove_nth_from_end
head = create_linked_list([1, 2, 3, 4, 5])
print("Original list:", print_linked_list(head))
modified = remove_nth_from_end(head, 2)  # Remove 2nd node from end (4)
print("After removing 2nd from end:", print_linked_list(modified))
print()

# -----------------------------------------------------------------------------
# 6. Add Two Numbers Represented by Linked Lists
# -----------------------------------------------------------------------------
def add_two_numbers(l1, l2):
    """
    Add two numbers represented by linked lists.
    The digits are stored in reverse order.
    
    Time Complexity: O(max(n, m))
    Space Complexity: O(max(n, m))
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        # Get values (or 0 if list ended)
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        
        # Calculate sum and carry
        total = x + y + carry
        carry = total // 10
        
        # Create new node with ones digit
        current.next = ListNode(total % 10)
        current = current.next
        
        # Move to next nodes if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next

# Test add_two_numbers
# Example: 342 + 465 = 807 (represented as 2->4->3 + 5->6->4 = 7->0->8)
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
sum_list = add_two_numbers(l1, l2)
print("Sum of lists:", print_linked_list(sum_list))
print()

# -----------------------------------------------------------------------------
# 7. Palindrome Linked List
# -----------------------------------------------------------------------------
def is_palindrome(head):
    """
    Check if the linked list is a palindrome.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return True
    
    # Find the middle of the linked list
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half
    second_half = reverse_linked_list(slow)
    
    # Compare first and second half
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True

# Test is_palindrome
palindrome = create_linked_list([1, 2, 3, 2, 1])
not_palindrome = create_linked_list([1, 2, 3, 4, 5])
print("Is [1,2,3,2,1] a palindrome?", is_palindrome(palindrome))
print("Is [1,2,3,4,5] a palindrome?", is_palindrome(not_palindrome))
print()

# -----------------------------------------------------------------------------
# 8. Intersection of Two Linked Lists
# -----------------------------------------------------------------------------
def get_intersection_node(headA, headB):
    """
    Find the node where two linked lists intersect.
    
    Time Complexity: O(n + m)
    Space Complexity: O(1)
    """
    if not headA or not headB:
        return None
    
    # Start pointers at the heads
    ptrA = headA
    ptrB = headB
    
    # Two-pointer technique: if one list reaches the end, 
    # redirect it to the beginning of the other list
    while ptrA != ptrB:
        # Move to next node or to the head of the other list
        ptrA = headB if ptrA is None else ptrA.next
        ptrB = headA if ptrB is None else ptrB.next
    
    # Either found intersection or both are null
    return ptrA

# Test get_intersection_node
common = create_linked_list([8, 9, 10])
headA = create_linked_list([1, 2, 3])
headB = create_linked_list([4, 5])

# Connect both lists to the common part
current = headA
while current.next:
    current = current.next
current.next = common

current = headB
while current.next:
    current = current.next
current.next = common

intersection = get_intersection_node(headA, headB)
print("Intersection node value:", intersection.val if intersection else None)
print()

# -----------------------------------------------------------------------------
# 9. Remove Duplicates from Sorted List
# -----------------------------------------------------------------------------
def delete_duplicates(head):
    """
    Remove all duplicates from a sorted linked list.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return head
    
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

# Test delete_duplicates
head = create_linked_list([1, 1, 2, 3, 3, 4, 5, 5])
print("With duplicates:", print_linked_list(head))
no_duplicates = delete_duplicates(head)
print("Without duplicates:", print_linked_list(no_duplicates))
print()

# -----------------------------------------------------------------------------
# 10. Swap Nodes in Pairs
# -----------------------------------------------------------------------------
def swap_pairs(head):
    """
    Swap every two adjacent nodes and return the head.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        
        # Swapping
        first.next = second.next
        second.next = first
        prev.next = second
        
        # Move to the next pair
        prev = first
    
    return dummy.next

# Test swap_pairs
head = create_linked_list([1, 2, 3, 4, 5])
print("Original list:", print_linked_list(head))
swapped = swap_pairs(head)
print("After swapping pairs:", print_linked_list(swapped))
print()

# -----------------------------------------------------------------------------
# 11. Partition List
# -----------------------------------------------------------------------------
def partition(head, x):
    """
    Partition list so all nodes less than x come before nodes >= x.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Create two dummy nodes for two lists
    before_dummy = ListNode(0)
    after_dummy = ListNode(0)
    
    # Pointers to track the two lists
    before = before_dummy
    after = after_dummy
    
    # Traverse the original list
    current = head
    while current:
        if current.val < x:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next
        current = current.next
    
    # Connect the two lists
    after.next = None  # Important to avoid cycles
    before.next = after_dummy.next
    
    return before_dummy.next

# Test partition
head = create_linked_list([1, 4, 3, 2, 5, 2])
print("Original list:", print_linked_list(head))
partitioned = partition(head, 3)
print("Partitioned around 3:", print_linked_list(partitioned))
print()

# -----------------------------------------------------------------------------
# 12. Sort Linked List (Merge Sort)
# -----------------------------------------------------------------------------
def sort_list(head):
    """
    Sort a linked list using Merge Sort.
    
    Time Complexity: O(n log n)
    Space Complexity: O(log n) for recursion stack
    """
    if not head or not head.next:
        return head
    
    # Find the middle of the linked list
    slow = head
    fast = head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Split the list into two halves
    mid = slow.next
    slow.next = None
    
    # Recursively sort both halves
    left = sort_list(head)
    right = sort_list(mid)
    
    # Merge the sorted halves
    return merge_two_lists(left, right)

# Test sort_list
head = create_linked_list([4, 2, 1, 3, 5])
print("Unsorted list:", print_linked_list(head))
sorted_head = sort_list(head)
print("Sorted list:", print_linked_list(sorted_head))
print()

# -----------------------------------------------------------------------------
# 13. Reorder List
# -----------------------------------------------------------------------------
def reorder_list(head):
    """
    Reorder list to L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return
    
    # Find the middle
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half
    prev = None
    current = slow
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    
    # Merge the two halves
    first = head
    second = prev
    
    while second.next:
        temp1 = first.next
        temp2 = second.next
        
        first.next = second
        second.next = temp1
        
        first = temp1
        second = temp2

# Test reorder_list
head = create_linked_list([1, 2, 3, 4, 5])
print("Original list:", print_linked_list(head))
reorder_list(head)
print("Reordered list:", print_linked_list(head))
print()

# -----------------------------------------------------------------------------
# 14. LRU Cache Implementation using Doubly Linked List
# -----------------------------------------------------------------------------
class LRUCache:
    """
    LRU Cache implementation using a doubly linked list and a hash map.
    
    Time Complexity: O(1) for both get and put operations
    Space Complexity: O(capacity)
    """
    class Node:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}  # key -> Node
        
        # Initialize dummy head and tail
        self.head = self.Node()  # Most recently used
        self.tail = self.Node()  # Least recently used
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        """Add node right after head (most recently used)"""
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """Remove an existing node from the linked list"""
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev
    
    def _move_to_head(self, node):
        """Move node to head (mark as most recently used)"""
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        """Remove the least recently used node (tail.prev)"""
        res = self.tail.prev
        self._remove_node(res)
        return res
    
    def get(self, key):
        """Get value by key and update to most recently used"""
        node = self.cache.get(key)
        if not node:
            return -1
        
        # Move to head (recently used)
        self._move_to_head(node)
        return node.value
    
    def put(self, key, value):
        """Add or update an entry and mark as most recently used"""
        node = self.cache.get(key)
        
        if not node:
            # Create new node
            new_node = self.Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1
            
            # Check capacity
            if self.size > self.capacity:
                # Remove the least recently used
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # Update existing node
            node.value = value
            self._move_to_head(node)

# Test LRU Cache
lru_cache = LRUCache(2)
lru_cache.put(1, 1)  # cache is {1=1}
lru_cache.put(2, 2)  # cache is {1=1, 2=2}
print("get(1):", lru_cache.get(1))  # returns 1
lru_cache.put(3, 3)  # evicts key 2, cache is {1=1, 3=3}
print("get(2):", lru_cache.get(2))  # returns -1 (not found)
lru_cache.put(4, 4)  # evicts key 1, cache is {4=4, 3=3}
print("get(1):", lru_cache.get(1))  # returns -1 (not found)
print("get(3):", lru_cache.get(3))  # returns 3
print("get(4):", lru_cache.get(4))  # returns 4
print()

# -----------------------------------------------------------------------------
# 15. Flatten a Multilevel Doubly Linked List
# -----------------------------------------------------------------------------
class Node:
    def __init__(self, val=None, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    """
    Flatten a multilevel doubly linked list.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head:
        return None
    
    # Pointer to traverse the list
    current = head
    
    while current:
        if current.child:
            # Save the next pointer
            next_temp = current.next
            
            # Connect current with child
            child = current.child
            current.next = child
            child.prev = current
            current.child = None  # Clear child pointer
            
            # Find the end of the child list
            child_tail = child
            while child_tail.next:
                child_tail = child_tail.next
            
            # Connect child tail with next
            if next_temp:
                child_tail.next = next_temp
                next_temp.prev = child_tail
        
        current = current.next
    
    return head

# Helper function to create a multilevel linked list for testing
def create_multilevel_list():
    # Create nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)
    
    # Connect main list
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3
    node4.next = node5
    node5.prev = node4
    node5.next = node6
    node6.prev = node5
    
    # Connect child list for node3
    node3.child = node7
    node7.next = node8
    node8.prev = node7
    node8.next = node9
    node9.prev = node8
    
    # Connect child list for node8
    node8.child = node11
    node11.next = node12
    node12.prev = node11
    
    # Connect child list for node9
    node9.child = node10
    
    return node1

# Print function for multilevel list
def print_multilevel_list(head):
    if not head:
        return "Empty list"
    
    result = []
    current = head
    while current:
        result.append(str(current.val))
        if current.child:
            result.append(f"({print_multilevel_list(current.child)})")
        current = current.next
    
    return "->".join(result)

# Print function for flattened list
def print_flattened_list(head):
    if not head:
        return "Empty list"
    
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    
    return "->".join(result)

# Test flatten
multilevel_head = create_multilevel_list()
print("Multilevel list:", print_multilevel_list(multilevel_head))
flattened_head = flatten(multilevel_head)
print("Flattened list:", print_flattened_list(flattened_head))
print()

# -----------------------------------------------------------------------------
# 16. Copy List with Random Pointer
# -----------------------------------------------------------------------------
class RandomNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    """
    Deep copy a linked list with next and random pointers.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not head:
        return None
    
    # Step 1: Create a copy of each node and insert it after the original node
    current = head
    while current:
        # Create the copy
        copy = RandomNode(current.val)
        
        # Insert the copy
        copy.next = current.next
        current.next = copy
        
        # Move to the next original node
        current = copy.next
    
    # Step 2: Assign random pointers for the copies
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        
        # Move to the next original node
        current = current.next.next
    
    # Step 3: Separate the original and copied lists
    original = head
    copy_head = head.next
    copy_current = copy_head
    
    while original:
        # Restore original list
        original.next = original.next.next
        
        # Update copy list
        if copy_current.next:
            copy_current.next = copy_current.next.next
        
        # Move to next nodes
        original = original.next
        copy_current = copy_current.next
    
    return copy_head

# Helper function to create a linked list with random pointers
def create_random_list():
    # Create nodes
    node1 = RandomNode(1)
    node2 = RandomNode(2)
    node3 = RandomNode(3)
    node4 = RandomNode(4)
    
    # Set next pointers
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    # Set random pointers
    node1.random = node3  # 1's random points to 3
    node2.random = node1  # 2's random points to 1
    node3.random = node4  # 3's random points to 4
    node4.random = node2  # 4's random points to 2
    
    return node1

# Test copy_random_list
print("Testing copy of list with random pointers")
original = create_random_list()
copied = copy_random_list(original)
print("Deep copy created successfully")
print()

# -----------------------------------------------------------------------------
# 17. Odd Even Linked List
# -----------------------------------------------------------------------------
def odd_even_list(head):
    """
    Group all odd-indexed nodes followed by even-indexed nodes.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return head
    
    odd = head
    even = head.next
    even_head = even
    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        
        even.next = odd.next
        even = even.next
    
    # Connect odd list with even list
    odd.next = even_head
    
    return head

# Test odd_even_list
head = create_linked_list([1, 2, 3, 4, 5])
print("Original list:", print_linked_list(head))
odd_even = odd_even_list(head)
print("Odd-even grouped list:", print_linked_list(odd_even))
print()

# -----------------------------------------------------------------------------
# 18. Remove Zero Sum Consecutive Nodes
# -----------------------------------------------------------------------------
def remove_zero_sum_sublists(head):
    """
    Remove all consecutive sequences of nodes that sum to 0.
    
    Time Complexity: O(n^2) in worst case
    Space Complexity: O(n)
    """
    # Dummy node to handle edge cases
    dummy = ListNode(0)
    dummy.next = head
    
    # Track prefix sums and their corresponding nodes
    prefix_sum = 0
    sum_to_node = {0: dummy}
    
    current = head
    while current:
        prefix_sum += current.val
        
        if prefix_sum in sum_to_node:
            # Remove nodes between sum_to_node[prefix_sum] and current
            to_delete = sum_to_node[prefix_sum].next
            temp_sum = prefix_sum
            
            # Delete all mappings of sums of nodes that will be removed
            while to_delete != current:
                temp_sum += to_delete.val
                if temp_sum != prefix_sum:  # Keep the original prefix_sum
                    del sum_to_node[temp_sum]
                to_delete = to_delete.next
            
            # Connect the nodes, skipping the zero-sum sequence
            sum_to_node[prefix_sum].next = current.next
        else:
            # Store this prefix sum
            sum_to_node[prefix_sum] = current
        
        current = current.next
    
    return dummy.next

# Test remove_zero_sum_sublists
head = create_linked_list([1, 2, -3, 3, 1])
print("Original list:", print_linked_list(head))
result = remove_zero_sum_sublists(head)
print("After removing zero sum sublists:", print_linked_list(result))

head2 = create_linked_list([1, 2, 3, -3, 4])
print("Original list:", print_linked_list(head2))
result2 = remove_zero_sum_sublists(head2)
print("After removing zero sum sublists:", print_linked_list(result2))
print()

# -----------------------------------------------------------------------------
# 19. Rotate List
# -----------------------------------------------------------------------------
def rotate_right(head, k):
    """
    Rotate the list to the right by k places.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next or k == 0:
        return head
    
    # Calculate length and find the last node
    current = head
    length = 1
    while current.next:
        current = current.next
        length += 1
    
    # Connect last node to the head to form a circle
    current.next = head
    
    # Adjust k if it's larger than the length
    k = k % length
    
    # Find the new tail: (length - k - 1)th node
    # New head will be the (length - k)th node
    current = head
    for _ in range(length - k - 1):
        current = current.next
    
    # Break the circle
    new_head = current.next
    current.next = None
    
    return new_head

# Test rotate_right
head = create_linked_list([1, 2, 3, 4, 5])
print("Original list:", print_linked_list(head))
rotated = rotate_right(head, 2)
print("After rotating right by 2:", print_linked_list(rotated))
print()

# -----------------------------------------------------------------------------
# 20. Reverse Nodes in k-Group
# -----------------------------------------------------------------------------
def reverse_k_group(head, k):
    """
    Reverse nodes in k-group.
    
    Time