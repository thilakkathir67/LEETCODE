def hash_map(s,t):
    if(len(s)!=len(t)):
        return False
    num={}
    for i in s:
        if i in num:
            num[i]+=1
        else:
        num[i]=1
    for i in t:
        if i not in num or num[i]==0:
            return False
        num[i]-=1
    return True
s=input()
t=input()
print(hash_map(s,t))