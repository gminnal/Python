#This program prints factorial of a number

num=int(input("Enter a number"))

fact=1
run=True

while run:
   if num>1:
    fact=fact*num
    num=num-1
   else:
    run=False


print("Factorial of a number Is", fact)



