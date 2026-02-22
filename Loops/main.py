# for i in range(st, end, skip):
#     operation to be performed multiple times.

# Range(num) : Ex. range(7) : 0,1,2,3,4,5,6
# Range(st,end) : Ex. range(2,6) : 2,3,4,5
# Range(st,end,skipNum) : Ex. range(3,11,2) : 3,5,7,9

list = ["Mumbai", "Delhi", "Surat", "Kolkata","Bengaluru", "Chennai"]
# Index:  0          1        2         3         4            5
# Access: list[0]  list[1]  list[2]  list[3]   list[4]       list[5]

# print(list) Traditional Way

# Printing all the elements of the list
for i in range(6):
    print(f"the value of i is {i}")
    print(list[i])

# Print Even index cities:
# Print

# Length function --> Gives the length of list.

list.append("Pune")


x = len(list)
print(f"The length of list is {x}")

list.append("Ahmedabad")
list.append("Lucknow")
list.append("Punjab")

# Using len(list) helps to dynamically print all the values.
for i in range(len(list)):
    print(list[i])


# Print the list in reverse order.

for i in range(len(list) - 1, -1, -1):
    print(list[i])


# Create or generate a list of even numbers from 1 to 50.

nums = []

for i in range(2,50,2):
    nums.append(i)

print(nums)