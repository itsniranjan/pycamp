# # input output
num = int(input("Enter a number: "))
string = str(input("Enter a string: "))
print(f"The number is: {float(num)}")

# conditional statements

if num > 0:
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")

# logical operators
if(num % 4 == 0 and num % 100 != 0) or (num % 100 == 0 and num % 400 == 0):
    print("The number is a leap year")

# looping statements
for i in range(1, 11):
    print(i)

while(num > 0):
    print(num)
    num -= 1


lst = [1, 2, 3, 4, 5]
# for i in lst:
#     print(i**2)

# tuple
tup = (1, 2, 3, 4, 5)  # any type of data can be stored in tuple
# set
set = {1, 2, 3, 4, 5}  # no duplicates, no order

# list comprehension
print(list(i*i for i in lst))

# lst.append(6)
# lst.extend([7,8,9])
# lst.insert(0, 0)
# lst.remove(9)
# lst.pop()
# lst.reverse()


# map(function, iterable)
def calculateSquare(n):
    return n*n


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(list(result))


# dictionary
d = {'a': 1, 'b': 2, 'c': 3}

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)
