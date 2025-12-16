def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number to find factorial: "))
print("Factorial of", num, "is", factorial(num))
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

base = int(input("Enter base: "))
exp = int(input("Enter power: "))
print("Result =", power(base, exp))

