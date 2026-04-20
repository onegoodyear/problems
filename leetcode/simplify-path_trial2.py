class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        def helper(i: int):
            if i < len(path):
                sub = ""
                while i < len(path) and path[i] == '/':
                    i += 1
                while i < len(path) and path[i] != '/':
                    sub += path[i]
                    i += 1
                if sub == ".":
                    helper(i+1)
                elif sub == "..":
                    if res: res.pop()
                    while res and res[-1] != '/': res.pop()
                    helper(i+1)
                else:
                    for c in sub: res.append(c)
                    if sub: res.append('/')
                    helper(i+1)
        
        helper(1)
        if res:
            res.pop()
            return '/' + ''.join(res)
        return '/'
        
                    
                    