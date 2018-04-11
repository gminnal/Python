numbers=[1,2,3,4,5,6,7,8]
for items in numbers:
    print(items)


current=1
run=True

while run:
    if current==100:
        run=False
    else:
        print(current)
        current=current+1


