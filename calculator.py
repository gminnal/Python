def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print("Choice")
print("1=>ADD")
print("2=>SUB")
print("3=>MULTIPLY")
print("4=>DIVISION")

ch=int(input("Enter your choice"))
num1=int(input("Enter First number"))
num2=int(input("Enter Second number"))

if ch==1:
    print(num1,"+", num2, "=", add(num1,num2))

elif ch==2:
    print(num1,"-", num2, "=", sub(num1,num2))

elif ch==3:
    print(num1,"*", num2, "=", mul(num1,num2))

elif ch==4:
    print(num1,"/", num2, "=", div(num1,num2))