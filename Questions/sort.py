# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or has a single node, return head
        if not head or not head.next:
            return head

        # Find the middle of the list
        mid = self.getMiddle(head)
        left = head
        right = mid.next
        mid.next = None  # Split the list into two halves

        # Recursively sort the left and right halves
        left = self.sortList(left)
        right = self.sortList(right)

        # Merge the two sorted halves
        return self.merge(left, right)

    # Helper function to find the middle of the list
    def getMiddle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Helper function to merge two sorted linked lists
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        # Merge two sorted lists
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        # If there are remaining nodes in either left or right list
        if left:
            tail.next = left
        if right:
            tail.next = right

        return dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
solution = Solution()

# Example 1
head = create_linked_list([4, 2, 1, 3])
sorted_head = solution.sortList(head)
print_linked_list(sorted_head)  # Output: 1 -> 2 -> 3 -> 4 -> None

# Example 2
head = create_linked_list([-1, 5, 3, 4, 0])
sorted_head = solution.sortList(head)
print_linked_list(sorted_head)  # Output: -1 -> 0 -> 3 -> 4 -> 5 -> None

# Example 3
head = create_linked_list([])
sorted_head = solution.sortList(head)
print_linked_list(sorted_head)  # Output: None
