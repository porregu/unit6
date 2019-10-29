def remove_duplicates(nums):
        for x in range(len(nums)-1):
            for y in range([x+1],len(nums)):
                if nums[y]==nums[x]:
                    del nums[y]
        return nums
print(remove_duplicates([1,2,2,1,2,3,2,3,3]))