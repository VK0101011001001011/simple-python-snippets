#Count the occurrence of each element in a list
numbers = [1, 2, 3, 2, 1, 3, 4, 2, 5, 1]
count = {}

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print("Element Count:", count)