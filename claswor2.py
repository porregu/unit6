
def are_duplicated(nums):
    for x in nums:
        for y in nums[x+1:]:
            if y==x:
                return True
    return False

are_duplicated([1, 2, 3, 4, 5])
print(are_duplicated([1,2,3,4,5,2]))
