def is_stored(nums):
    for x in range(len(nums)):
        if nums[x]<=nums[x+1]:
            return True
        if nums[x]>nums[x+1]:
            return False
print(is_stored(["a","b","c"]))