a=1234567
sqr=1000
n=3
c=2*n
p=0
while p!=1.0:
    p=round(a/(sqr**2), c)
    if a>sqr**2:
        sqr=sqr+10**n
    else:
        sqr=sqr-10**n
        n=n-1
print(sqr)
