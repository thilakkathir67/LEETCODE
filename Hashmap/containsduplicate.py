def hash_map(n):
    num={}
    for i in n:
        if i in num:
            return True
        num[i]=1
    return False
    
n=[2,5,10,15]

print(hash_map(n))