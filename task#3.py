"""Author;savio bijo thomas
   date:3-12-24
   purpose:multiplying two numbers using recursion"""

def multi_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multi_numbers(n1,n2-1)
m=multi_numbers(20,30)
print(m)

