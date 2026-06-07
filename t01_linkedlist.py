"""
Task 01
LinkedList:
- work only with numerical data
"""
class Node:
    """Single Node of LinkedList. A"""
    def __init__(self, data):
        if not isinstance(data, (int, float)) or isinstance(data, bool):
            raise TypeError(
                f"Node accept only integers or float."
                f"Received type: \"{type(data).__name__!r}\""
            )
        self.data = data
        self.next = None

class LinkedList:
    """Linked List with basic methods."""
    
    def __init__(self):
        self.head = None 

    def append(self, value: int | float) -> None:
        """Add Node to the end to the LinkedList"""
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head 
        while current.next:
            current = current.next
        current.next = node 
    
    def to_list(self) -> list:
        """Return LinkedList as list"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __repr__(self) -> str:
        return " -> ".join(map(str, self.to_list()))
    
    # Requirement 01: Reverse
    def reverse(self) -> None:
        """
            Reverse LinkedList, change direction between Nodes.
            Complexity: Time - O(n) | Space O(1)
        """ 
        previous = None 
        current = self.head
        while current:
            next_node = current.next 
            current.next = previous
            previous = current
            current = next_node         
        self.head = previous            # new head -- previous tail

    # Requirement 02: Insertion sorting
    def insertion_sort(self) -> None:
        """
            Insertion sorting for LinkedList.
            Complexity: Time - O(n^2) | Space O(1)
        """
        sorted_head = None 
        current = self.head
        while current:
            next_node = current.next
            sorted_head = _sorted_insert(sorted_head, current)
            current = next_node
        self.head = sorted_head
    

def _sorted_insert(sorted_head: Node | None, node: Node) -> Node:
    """Insert Node in sorted list, return new head."""
    node.next = None
    if not sorted_head or node.data <= sorted_head.data:
        node.next = sorted_head
        return node
    current = sorted_head
    while current.next and current.next.data < node.data:
        current = current.next
    node.next = current.next
    current.next = node
    return sorted_head

# Requirements 03: Merge two sorted lists
def merge_sorted(head1: Node | None, head2: Node | None) -> Node | None:
    """
        Merge two sorted LinkedLists to one sorted LinkedList. 
        Complexity: Time - O(n + m), Space - O(1)  
    """
    dummy = Node(0)
    tail = dummy
    a, b = head1, head2
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next 
    tail.next = a if a else b
    return dummy.next

# Demonstration 
def demo():
    print("\n", "~" * 5, " LINKED LIST ", "~" * 5)
 
    # 1. Reverse: 
    print(f"\nReverse a LinkedList {"-" * 32}")
    l_list_01 = LinkedList()
    for v in [5, 3, 8, 1, 6]:
        l_list_01.append(v)
    print(f" Before:  {l_list_01}")
    l_list_01.reverse()
    print(f"  After:  {l_list_01}")
 
    # 2. Insertion sorting
    print(f"\nInsertion sorting {"-" * 35}")
    l_list_02 = LinkedList()
    for v in [7, 2.5, 9, 4.1, 1, 6]:
        l_list_02.append(v)
    print(f" Before:  {l_list_02}")
    l_list_02.insertion_sort()
    print(f"  After:  {l_list_02}")
 
    # 3. Merge of two sorted LinkedLists
    print(f"\nSorted LinkedLists Merge {"-" * 28}")
    list_a = LinkedList()
    list_b = LinkedList()
    vals_a = [1, 4, 7, 11]
    vals_b = [2, 5, 8, 10, 14]
    for v in vals_a:
        list_a.append(v)
    for v in vals_b:
        list_b.append(v)
    print(f"  A:      {list_a}")
    print(f"  B:      {list_b}")
    merged_head = merge_sorted(list_a.head, list_b.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    print(f"  Merged: {merged_list}")
    assert merged_list.to_list() == sorted(vals_a + vals_b)
 
    # 4. Extra data type validation
    print(f"\nData type validation {"-" * 32}")
    invalid_cases = [
        ("String", "hello"),
        ("List", [1, 2]),
        ("None", None),
        ("bool", True),
    ]
    for label, val in invalid_cases:
        try:
            test_node = LinkedList()
            test_node.append(val)
            print(f"  [FAIL] {label:<6} -> should raise TypeError!")
        except TypeError as e:
            print(f"  [OK]   {label:<6} → {e}")
 

if __name__ == "__main__":
    demo()