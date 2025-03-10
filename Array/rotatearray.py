nums=[1,2,3,4,5]
k=1
k=k%(len(nums))
nums[:]=nums[-k:]+nums[:-k]
print(nums)
        