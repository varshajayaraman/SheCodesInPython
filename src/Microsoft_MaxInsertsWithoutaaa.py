def sol(s):
    c=""
    for x in s:
        c+=x
    count = 0
    if s[0]!='a':
        count+=2
        c = 'aa'+c
    for i in range(1,len(s)):
        if s[i]=='a' and i + 1 < len(s) and s[i + 1] == 'a' and s[i - 1] == 'a':
            print(-1)
            return
        if s[i]=='a' and s[i-1]!='a':

            if i==len(s)-1 or s[i+1]!='a':
                count +=1
                c = c[:i]+'a'+c[i:]

        else:
            if s[i]!='a' and s[i-1]!='a':
                count+=2
                print(c)
                c = c[:i]+'aa'+c[i:]
                print(c)
    if s[len(s)-1]!='a':
        count +=2
        c+='aa'
    print(count, c)