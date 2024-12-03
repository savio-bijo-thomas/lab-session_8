"""Author;savio bijo thomas
   date:3-12-24
   purpose:greatest common divisor"""

def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
g=gcd(50,40)
print(g)