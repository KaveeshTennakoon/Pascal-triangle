num=int(input("Enter the number of rows: "))

for i in range(1,num+1):
    print(" " * ((num+1) - i -1),end="")
    value = 1
    for j in range(1,i+1):
        print(value,end=" ")
        value=value*(i-j)//j
    print()
