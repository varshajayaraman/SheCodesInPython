def solution(s):
    def find(s,ch,index):
        st = index
        while index<len(s):
            if s[index] == ch:
                index+=1
            else:
                if st == index:
                    return -1
                else:
                    return index
        return index
    i=0
    while i < len(s)-2:
        if s[i] == s[i+1] == s[i+2]:
            j=find(s,s[i],i+3)
            if j != -1:
                lastind=i
                s = s[:i]+s[j:]
                print(s)
                i=lastind-1
                continue
            else:
                s=s[:i]+s[i+3:]
                print(s)
                i=0
                continue
        i+=1
    print(s)