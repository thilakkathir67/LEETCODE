def hash_map(n,t):
    num={}
    for i,j in enumerate(n):
        complement=t-j
        if complement in num:
            return [num[complement],i]
        num[j]=i
    return[]
    
n=[2,5,10,12,15]
t=9
print(hash_map(n,t))