def hashmap(s,t):
    num1={}
    num2={}
    if len(s)!=len(t):
        return False
    for i in range(len(s)):
        c1=s[i]
        c2=t[i]
        
        if c1 in num1 and num1[c1]!=c2:
            return False
        if c2 in num2 and num2[c2]!=c1:
            return False
        
        num1[c1]=c2
        num2[c2]=c1
    return True
s=input()
t=input()
print(hashmap(s,t))