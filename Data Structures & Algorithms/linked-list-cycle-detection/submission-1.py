# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        cur = head

        index_slow = cur
        index_fast = cur
        while index_slow and index_fast and index_fast.next:
            
            index_slow = index_slow.next
            index_fast = index_fast.next.next
            if index_slow == index_fast:
                return True

        return False
        