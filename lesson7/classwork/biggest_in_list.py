nums = [1, 5, 3, 9, 2] # example list
print(nums)# print the list

biggest_item = max(nums)# find the biggest item
sallest_item = min(nums)# find the smallest item

print("Biggest item:", biggest_item)# print the biggest item
print("Smallest item:", sallest_item)# print the smallest item

print("Our algorithm:")# print a message

nums2 = [2, 4, 1, 7, 3]# example list 2
print(nums2)# print the list

biggest = nums2[0] # start by assuming the first item is the biggest

for i in range(len(nums2)):# loop through all items
    if nums2[i] > biggest:# compare each item with the current biggest
        biggest = nums2[i]# update biggest if current item is larger

print('The biggest item is:', biggest)# print the biggest item found by the algorithm

nums3 = [23, 11, 45, 7, 32, 19]# example list 3
for i in range(len(nums3)): # loop through all items
    if nums3[i] > smallest:
        smallest = nums3[i]