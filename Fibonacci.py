#Printing Fibonacci Series
a=1
b=1
c=a+b
print(a)
print(b)

run=True

while run:
    if c<=30:
        print(c)
        a=b
        b=c
        c=a+b
    else:
        run=False
