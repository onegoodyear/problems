# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reminder = 0
        dummy = ListNode()
        dummy.next = ListNode()
        p = dummy
        while l1 and l2:
            p = p.next
            t = l1.val + l2.val + reminder
            if t > 9: 
                reminder = 1
                t -= 10
            else:
                reminder = 0
            p.val = t
            p.next = ListNode()
            l1 = l1.next
            l2 = l2.next
        if l2: l1 = l2
        while l1:
            p = p.next
            t = l1.val + reminder
            if t > 9: 
                reminder = 1
                t -= 10
            else: reminder = 0
            p.val = t
            p.next = ListNode()
            l1 = l1.next
        if reminder:
            p.next.val = 1
        else: p.next = None
        return dummy.next
        # return res


        