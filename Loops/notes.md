# 📘 Python Loops and List Handling -- Notes

## 🔹 1. Basic Structure of a `for` Loop

``` python
for i in range(st, end, skip):
    # operation to be performed multiple times
```

------------------------------------------------------------------------

## 🔹 2. Understanding `range()` Function

### ✅ `range(num)`

Starts from 0 and goes up to (num - 1)

``` python
range(7) → 0,1,2,3,4,5,6
```

------------------------------------------------------------------------

### ✅ `range(start, end)`

Starts from `start` and stops before `end`

``` python
range(2,6) → 2,3,4,5
```

------------------------------------------------------------------------

### ✅ `range(start, end, skip)`

Skips numbers based on step value

``` python
range(3,11,2) → 3,5,7,9
```

------------------------------------------------------------------------

# 🔹 3. Working with Lists

## Creating a List

``` python
cities = ["Mumbai", "Delhi", "Surat", "Kolkata", "Bengaluru", "Chennai"]
```

### Index Positions:

  Index   Value
  ------- -----------
  0       Mumbai
  1       Delhi
  2       Surat
  3       Kolkata
  4       Bengaluru
  5       Chennai

------------------------------------------------------------------------

## 🔹 4. Printing List Elements (Traditional Way)

``` python
for i in range(6):
    print(f"the value of i is {i}")
    print(cities[i])
```

⚠️ Not dynamic --- if list size changes, this must be updated.

------------------------------------------------------------------------

# 🔹 5. Using `len()` Function (Dynamic Way)

`len(list)` gives the total number of elements.

``` python
x = len(cities)
print(f"The length of list is {x}")
```

------------------------------------------------------------------------

## Adding Elements to a List

``` python
cities.append("Pune")
cities.append("Ahmedabad")
cities.append("Lucknow")
cities.append("Punjab")
```

------------------------------------------------------------------------

## Dynamic Printing Using `len()`

``` python
for i in range(len(cities)):
    print(cities[i])
```

✅ Best practice --- automatically adjusts to list size.

------------------------------------------------------------------------

# 🔹 6. Printing List in Reverse Order

``` python
for i in range(len(cities) - 1, -1, -1):
    print(cities[i])
```

Explanation: - Start from last index - Stop before -1 - Step = -1 (move
backwards)

------------------------------------------------------------------------

# 🔹 7. Generating Even Numbers from 1 to 50

``` python
nums = []

for i in range(2, 50, 2):
    nums.append(i)

print(nums)
```

Explanation: - Start at 2 - Stop before 50 - Step size 2 (even
numbers) - Append each number to list

------------------------------------------------------------------------

# 🔹 Key Concepts Summary

✔ `range()` controls loop iterations\
✔ `len()` makes loops dynamic\
✔ `append()` adds elements to list\
✔ Negative step allows reverse iteration\
✔ Loops help automate repetitive tasks


