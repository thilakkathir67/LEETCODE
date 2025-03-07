nums = [1, 2, 3, -1, 4]
k = 3
hashmap = {0: 1}  
prefix_sum = 0
count = 0

for num in nums:
    prefix_sum += num
    
   
    if prefix_sum - k in hashmap:
        count += hashmap[prefix_sum - k]  
    
   
    if prefix_sum in hashmap:
        hashmap[prefix_sum] += 1
    else:
        hashmap[prefix_sum] = 1  

    print(f"num={num}, prefix_sum={prefix_sum}, hashmap={hashmap}, count={count}")

print(f"Total subarrays with sum {k}: {count}")
