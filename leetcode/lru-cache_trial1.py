class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
         

    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.prev.next = node
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev = node
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.get(key)          
        else:
            if len(self.cache) == self.capacity:
                removed = self.head.next
                del self.cache[removed.key]
                self.head.next = removed.next
                removed.next.prev = self.head
                removed.key = key
                removed.val = value
                removed.next = self.tail
                removed.prev = self.tail.prev
                self.tail.prev.next = removed
                self.tail.prev = removed
                self.cache[key] = removed
            else:
                new = Node(key,value)
                new.next = self.tail
                new.prev = self.tail.prev
                self.tail.prev.next = new
                self.tail.prev = new
                self.cache[key] = new


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)