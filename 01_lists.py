'''
marks = [54, 23, 64, 93, 32]
mixed = [43, "Hello", False, 4.2]

print(marks[2:4])
print(marks[2])
print(mixed[4]) # Error Index out of bound
'''

'''
What is a List in Python?

A list is a collection used to store multiple values in a single variable.

✔ Ordered
✔ Changeable (mutable)
✔ Allows duplicate values
✔ Can store different data types

List is a collection of values

Index always starts from 0

list[i] → single value

list[a:b] → slice (a included, b excluded)

'''




# List that stores students' marks
marks = [54, 23, 64, 93, 32]

# 1. Question: What is the first mark?
print("1. What is the first mark?")
# marks[0] gives the value at index 0 (first element)
print(marks[0])


# 2. Question: What is the last mark?
print("2. What is the last mark?")
# -1 refers to the last element in the list
print(marks[-1])


# 3. Question: What is the highest mark?
print("3. What is the highest mark?")
# max() returns the largest value from the list
print(max(marks))


# 4. Question: What is the lowest mark?
print("4. What is the lowest mark?")
# min() returns the smallest value from the list
print(min(marks))


# 5. Question: How many marks are there?
print("5. How many marks are there?")
# len() returns the total number of elements in the list
print(len(marks))


# 6. Question: What mark is at index 2?
print("6. What mark is at index 2?")
# marks[2] gives the value stored at index 2
print(marks[2])


# 7. Question: What are the marks from index 2 to 4?
print("7. What are the marks from index 2 to 4?")
# Slicing: start from index 2 and stop before index 4
print(marks[2:4])





# 8. Question: What is the average of all marks?
print("9. What is the average of all marks?")
# sum() adds all marks, len() counts them, division gives average
print(sum(marks) / len(marks))



