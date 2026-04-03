# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(-201, head)
        left = dummy
        right = head
        prev = dummy
        while right:
            if right.val < x:
                if right == left.next:
                    left = left.next
                    prev = prev.next
                    right = right.next
                else:
                    tl = left.next
                    tr = right.next
                    #updating the left by adding the right node:
                    left.next = right
                    right.next = tl
                    left = left.next
                    #updating the right by removing the right node:
                    prev.next = tr
                    right = tr
            else:
                prev = prev.next
                right = right.next

        return dummy.next

        