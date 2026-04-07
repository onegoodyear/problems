# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev = dummy
        while prev.next and prev.next.next:
            temp = prev.next.next
            prev.next.next = prev.next.next.next
            temp.next = prev.next
            prev.next = temp
            prev = prev.next.next
        return dummy.next

            