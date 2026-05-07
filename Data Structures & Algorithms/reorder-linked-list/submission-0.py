# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(head_new: Optional[ListNode]) -> Optional[ListNode]:
            cur = head_new
            prev = None
            while cur:
                cur_tmp = cur.next
                cur.next = prev
                prev = cur
                cur = cur_tmp
            return prev

        cur = head

        index_slow = head
        index_fast = head
        while index_fast.next and index_fast.next.next:
            index_slow = index_slow.next
            index_fast = index_fast.next.next
        
        head_split = index_slow.next
        index_slow.next = None

        head_split_reversed = reverseList(head_split)

        while cur:
            prev = cur.next
            cur.next = head_split_reversed
            cur = cur.next
            head_split_reversed = prev

        