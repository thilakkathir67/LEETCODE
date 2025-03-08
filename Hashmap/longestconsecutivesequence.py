nums = [100, 4, 200, 1, 3, 2]

hashmap = {}  
for num in nums:
    hashmap[num] = True  

longest = 0

for num in nums:
    if num - 1 not in hashmap: 
        length = 1
        while num + length in hashmap:
            length += 1
        longest = max(longest, length)

print(longest)  
