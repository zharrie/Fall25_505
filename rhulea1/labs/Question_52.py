def get_max_int(nums)
# Assume first number is the highest
 maximum = nums[0]
    for n in nums:
        if n > maximum:
            maximum = n
    return maximum
#Collect numbers into list until -1 is entered
nums = []
    while True
     value = int(input())
     if value == -1
        break
    nums.append(value)
#Finding the maximum value
max_value = get_max_value(nums)
# Each value is subtracted from the maximum value
for n in nums
    print(max_value - n)
