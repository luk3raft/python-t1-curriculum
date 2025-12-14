nums = [5, -8, 35, -3, 6, 2]
print(nums)

total = sum(nums)
print("Sum:", total)

print("our algorithm:")

total = 0
for i in range(len(nums)):  # iterate through each index in the list
    item = nums[i]  # get the item at that index
    total = total + item  # add the item to the total
print("Sum:", total)

total = 0
for i in range(len(nums)):
    item = nums[i]
    if item > 0:
        total = total + item
print("Sum of positive numbers:", total)
