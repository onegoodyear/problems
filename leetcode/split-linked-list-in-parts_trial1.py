# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        sz = 0
        p = head
        while p:
            sz += 1
            p = p.next
        ll = sz // k
        addons = sz % k
        res = []
        curr = head
        for _ in range(k):
            if curr:
                counter = 1
                res.append(curr)
                while curr.next and counter < ll + (addons > 0):
                    curr = curr.next
                    counter += 1
                else:
                    temp = curr.next
                    curr.next = None
                    curr = temp
                    addons -= 1
            else:
                res.append(None)
        return res