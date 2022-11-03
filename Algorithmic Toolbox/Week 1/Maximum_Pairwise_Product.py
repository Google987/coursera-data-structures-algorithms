element_count = int(input())
nums = input().split()

nums = [int(x) for x in nums]

max1_index = 0
for index in range(element_count):
    if nums[index] > nums[max1_index]:
        max1_index = index

max2_index = 0 if max1_index != 0 else 1
for index in range(element_count):
    if max1_index != index and nums[index] > nums[max2_index]:
        max2_index = index

print(nums[max1_index] * nums[max2_index])

