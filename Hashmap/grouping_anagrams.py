def hashmap(s):
    num={}
    for i in s:
        fr =[0]*26
        for j in i:
            index=ord(j)-ord('a')
            fr[index]+=1
        key=tuple(fr)
        if key in num:
            num[key].append(i)
            
        else:
            num[key]=[i]
    return list(num.values())
            
s=["tea","eat","bat","tan","nat"]
print(hashmap(s))