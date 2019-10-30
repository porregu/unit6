def get_min(nums):
    min_number = nums[0]
    for y in (nums):
        if y < min_number:
            min_number = y
    return min_number
print(get_min([3,4,12,12233,23,3]))