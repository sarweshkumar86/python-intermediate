marks = [5, 2, 21, 5, 7]
extra_marks = [53, 23, 32]

print(marks)
# marks.append(63) # This will change the original list
# marks.pop()
marks.extend(extra_marks)
print(marks)


# Initial list
marks = [5, 2, 21, 5, 7]

# 1. Question: How to add a new mark at the end?
print("1. How to add a new mark at the end?")
# append() adds one element at the end of the list
marks.append(10)
print(marks)


# 2. Question: How to add multiple marks at once?
print("2. How to add multiple marks at once?")
# extend() adds all elements of another list
marks.extend([15, 20])
print(marks)


# 3. Question: How to add a mark at a specific position?
print("3. How to add a mark at index 2?")
# insert(index, value) adds value at given index
marks.insert(2, 99)
print(marks)


# 4. Question: How to remove the last mark?
print("4. How to remove the last mark?")
# pop() removes the last element
marks.pop()
print(marks)


# 5. Question: How to remove a mark from a specific index?
print("5. How to remove mark at index 1?")
# pop(index) removes element from given index
marks.pop(1)
print(marks)


# 6. Question: How to remove a specific value?
print("6. How to remove value 5?")
# remove(value) removes the first occurrence of that value
marks.remove(5)
print(marks)


# 7. Question: How to check if a value exists in the list?
print("7. How to check if 21 exists in the list?")
# in keyword checks presence of a value
print(21 in marks)


# 8. Question: How to count how many times a value appears?
print("8. How many times does 5 appear?")
# count() returns number of occurrences
print(marks.count(5))


# 9. Question: How to sort the list?
print("9. How to sort the marks list?")
# sort() arranges the list in ascending order
marks.sort()
print(marks)


# 10. Question: How to remove all elements from the list?
print("10. How to clear the list?")
# clear() removes all elements from the list
marks.clear()
print(marks)
