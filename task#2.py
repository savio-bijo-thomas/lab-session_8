"""Author;savio bijo thomas
   date:3-12-24
   purpose:adding two numbers using recursion"""


def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
         return add_numbers(n1+1,n2-1)
sum=add_numbers(20,30)
print(sum)