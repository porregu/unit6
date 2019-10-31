def lis(nums):
    blank_list=[]
    for y in nums:
        if y not in blank_list:
            blank_list.append(nums[0])
        if y%nums!=0 :
                return blank_list
    print(lis)
print(lis([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))