def hashmap(l1,l2):
    num={}
    result=[]
    for i in l1:
        num[i]=True
    for i in l2:
        if i in num:
            result.append(i)
            del num[i]
    return result


l1=[1,2,3,4,5]
l2=[1,2,1,2,3]
print(hashmap(l1,l2))
