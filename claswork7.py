def get_max(nums):
    max_number=0
    for y in(nums):
        if y>max_number:
            max_number=y
    return max_number
print(get_max([1,3,4,12,1,12233,23,3]))