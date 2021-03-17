nums = [1,2,3,1,1,3]

a = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print(i, j)
            a += 1
print(a)