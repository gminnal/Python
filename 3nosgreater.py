#Print greater of three numbers

num1=int(input("Enter First Number"))
num2=int(input("Enter Second Number"))
num3=int(input("Enter Third number"))

if num1>num2 and num1>num3:
    print("First Number is greater")
elif num2>num1 and num2>num3:
    print("Second number is greater")
elif num3 > num1 and num3 > num2:
    print("Third Number is greater")
elif num3 == num1 and num3 == num2:
    print("All numbers are equal")