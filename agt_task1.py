a = int(input("enter the value to find its factorial: "))
def factorial(n):
    if n < 2:
        return 1
    else:
       return n * (factorial(n-1))
result = factorial(a)
print(result)
