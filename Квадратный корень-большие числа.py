print("square root comput: v1.0 by Alexey Pushkin 22.04.2017")
print("Square Root Comput")
a=float(input("Input the number (>0): "))
if a==str():
    print("String object detected")
elif a<0:
    print("Error: the number is less than zero")
elif a==0:
    print("The ansver is zero: 0")

p=0
b=1
n=-1
while b<=a:
    b=b*10
    n=n+1 
c=5+n*2
sqr=10**abs(n/2)
while p!=1.0:
    p=round(a/(sqr**2), c)
    if a>sqr**2:
        sqr=sqr+10**n
    else:
        sqr=sqr-10**n
        n=n-1
print("The square Root is: ",sqr)
