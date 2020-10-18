class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        def populate(str):
            d = {}
            v = {}
            for s in str:
                v[s] = False
                if not d.get(s):
                    d[s] = 1
                else:
                    d[s] += 1
            return d,v
        
        cnt = {}
        cnt, visited = populate(s)
        stack = []
        
        for ch in s:
            cnt[ch] -=1
            # if visited[ch]:
            #     continue
            if visited[ch]:
                continue
            while len(stack)>0 and ch<stack[-1] and cnt[stack[-1]]>0:
                print(stack, ch)
                visited[stack[-1]] = False
                stack.pop()
                
            stack.append(ch)
            visited[ch] = True
            
        return "".join(stack)