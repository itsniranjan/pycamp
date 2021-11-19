# string formatting

import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
now = datetime.datetime.now()
print(my_date)

sentence = '{:%B %d, %Y}'.format(my_date)
today = '{:%B %d, %Y}'.format(now)
print(sentence)
print(today)

str1 = "hello"
str2 = "world"

# concatenation
print(str1+str2)

# length of string
print(len(str1))

# character count
print(str1.count('l'))

# splitting
print(str1.split('_'))

# remove trailing or leading spaces (or characters)
print(str1.strip())

# change case
print(str1.upper())  # .lower(), .title(), .swapcase()

# only has alphanumeric characters
print(str1.isalnum())  # .isalpha(), .isdigit(), .islower(), .isupper()

# startswith()
print(str1.startswith('h'))

# join
print('_'.join([str1, str2]))  # tuple/list or any iterable as parameter

# fill with zeros
print(str1.zfill(10))  # 10 is the length of the new string

# search for substrings
# returns the index of the first occurrence of the substring
print(str1.find('l'))

# slicing
# returns the substring starting at index 0 and ending at index 3
print(str1[0:3])
# negative indexing
print(str1[-1])  # returns the last character
# slicing with step
# returns the substring starting from first and ending at index 5 with a step of 2
print(str1[:5:2])
