# def divide(x, y):
#     try:
#         # Floor Division : Gives only Fractional Part as Answer
#         result = x // y
#         print("Yeah ! Your answer is :", result)
#     except ZeroDivisionError:
#         print("Sorry ! You are dividing by zero ")

# # Look at parameters and note the working of Program
# divide(3, 0)

try:
    f = open('corrupt_file.txt', 'r')
    print(f.readlines())
    # if f.name == 'corrupt_file.txt':
    #     raise Exception
except IOError as e:
    print('Check filename again!')
except Exception as e:
    print('corrupted!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')
f.close()
