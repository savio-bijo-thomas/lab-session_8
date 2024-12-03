"""Author;savio bijo thomas
   date:3-12-24
   purpose:factorial of a number using recursion """



def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
f=factorial(5)
print(f)
