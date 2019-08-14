def max_num(num1,num2,num3):
    if num1 >= num2 and num1>=num3:
        print(num1,"is the max numnber")
    elif num2>=num3:
        print(num2,"is the max number")
    else:
        print(num3,"is the max number")
a=int(input("Enter the number1"))
b=int(input("Enter the number2"))
c=int(input("Enter the number3"))
max_num(a,b,c)