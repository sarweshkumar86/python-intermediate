'''
What is a Tuple?
A tuple is a collection of items in Python that is ordered and immutable.

1.  Tuple is represented using parentheses ()
    t = (10, 20, 30)

2.  Tuple is immutable (cannot be changed)
    t = (1, 2, 3)
    t[0] = 10   # ❌ Error
    
3. Tuple can store multiple data types

    t = (1, "Hello", True, 3.5)


4. Tuple allows duplicate values
    t = (5, 5, 10)

    
What is Tuple Unpacking?

 Tuple unpacking is the process of assigning tuple values to multiple variables in a single statement.

  Tuple Unpacking Example
  t = (3, 2, 45)
  a, b, c = t

  a = 3
  b = 2
  c = 45

Important Points about Tuple Unpacking

5. Number of variables must match the number of tuple elements

  a, b = (1, 2, 3)   # ❌ ValueError


'''




tu = (3, 2, 45)

a, b, c = tu 

print(a, b, c)



# def get_result(marks):
#     total = sum(marks)
#     avg = total / len(marks)
#     return total, avg

# total, average = get_result([60, 70, 80])
# print(total, average)
