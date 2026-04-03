# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        left = head
        right = head.next
        while right:
            if right.val == left.val:
                right = right.next
                left.next = right
            else:
                left = left.next
                right = right.next
        return head
        