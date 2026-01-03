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




# List of marks
marks = [54, 23, 64, 93, 32]

# 1. Question: What is the first mark?
print("1. What is the first mark?")
# marks[0] means index 0 ka value (first element)
print(marks[0])


# 2. Question: What is the last mark?
print("2. What is the last mark?")
# -1 ka matlab last element
print(marks[-1])


# 3. Question: What is the highest mark?
print("3. What is the highest mark?")
# max() function list ka sabse bada number deta hai
print(max(marks))


# 4. Question: What is the lowest mark?
print("4. What is the lowest mark?")
# min() function list ka sabse chhota number deta hai
print(min(marks))


# 5. Question: How many marks are there?
print("5. How many marks are there?")
# len() function list me total elements count karta hai
print(len(marks))


# 6. Question: What mark is at index 2?
print("6. What mark is at index 2?")
# marks[2] means index 2 ka value
print(marks[2])


# 7. Question: What are the marks from index 2 to 4?
print("7. What are the marks from index 2 to 4?")
# slicing: index 2 se start, 4 se pehle tak
print(marks[2:4])


# 8. Question: Are there any marks below 40?
print("8. Are there any marks below 40?")
# loop ke through 40 se chhote marks nikal rahe hain
print([m for m in marks if m < 40])


# 9. Question: What is the average of all marks?
print("9. What is the average of all marks?")
# sum() se total, len() se count, phir divide
print(sum(marks) / len(marks))


# 10. Question: Are all marks above 50?
print("10. Are all marks above 50?")
# all() check karta hai sab values 50 se badi hain ya nahi
print(all(m > 50 for m in marks))
