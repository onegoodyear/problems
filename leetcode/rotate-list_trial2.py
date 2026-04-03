# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def reverse(head: ListNode, start: int, end: int) -> (ListNode, ListNode):
#             q, p = head, None
#             for _ in range(1, start): 
#                 p = q
#                 q = q.next
#             i = start - 1
#             prev, curr = p, q
#             while i < end:
#                 i += 1
#                 temp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = temp
#             return prev,curr

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        t, sz = head, 0
        while t:
            t = t.next
            sz += 1
        if sz == 0: return None
        k = k % sz
        prev = head
        for _ in range(1, sz - k): prev = prev.next
        right, left = prev.next, head
        prev.next = None
        t = right
        while t and t.next: t = t.next
        if t: t.next = left
        return right or left
        

        