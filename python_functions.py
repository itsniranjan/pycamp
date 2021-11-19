# Arbitrary Arguments are often shortened to *args
def find_mean(*args):
    print(f"The mean is {(sum(args)/len(args))}")


find_mean(11, 31, 51, 7, 9)

# Keyword Arguments are often shortened to **kwargs


def json_convert(**kid):
    json_string = f'"fname":"{kid["fname"]}","lname":"{kid["lname"]}"'
    return json_string


json_mode = json_convert(fname="Ravi", lname="Tharakan")
print(json_mode)


# if for some reason you want a function with no content, pass
def myfunction():
    pass


# recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


# tail recursion
def factorial(n, result=1):
    if n == 1:
        return result
    else:
        return factorial(n-1, n*result)


# scope -- global and local
for a in range(2):
    x = 'global {}'.format(a)


def outer():
    # x = 'outer x'
    for b in range(3):
        x = 'outer {}'.format(b)

    def inner():
        # x = 'inner x'
        for c in range(4):
            x = 'inner {}'.format(c)
        print(x)
        print(a, b, c)

    inner()
    print(x)
    print(a, b)


outer()
print(x)
print(a)
