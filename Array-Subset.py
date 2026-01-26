# Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        d = {}
        for x in a:
            d[x] = d.get(x, 0) + 1
        
        for y in b:
            if d.get(y,0) == 0: return False
            d[y] -= 1
        
        return True
    