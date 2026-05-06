# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_new = ListNode()
        head = cur_new
        cur1 = list1
        cur2 = list2
        while cur1 or cur2:
            if cur2 == None or (cur1 != None and cur1.val <= cur2.val):
                cur_new.next = cur1
                cur1 = cur1.next
            else:
                cur_new.next = cur2
                cur2 = cur2.next
            cur_new = cur_new.next
        
        return head.next
        