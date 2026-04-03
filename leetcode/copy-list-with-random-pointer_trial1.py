"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        q = head
        while q:
            new = Node(x =  q.val, next = q.next)
            q.next = new
            q = new.next
        q = head
        while q:
            if q.random:
                q.next.random = q.random.next
            q = q.next.next
        dummy = Node(10001, next = head)
        q = dummy
        while q and q.next:
            q.next = q.next.next
            q = q.next
        return dummy.next

        
            