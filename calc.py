loop =1
choice=0
while loop==1:
    choice=int(input("choose the option"))
    print("the choice is",choice)
    if choice==1:
        add1=int(input("Enter number1"))
        add2=int(input("Enter number2"))
        sum1=add1+add2
        print("The value is",sum1)
    elif choice==2:
        sub1=int(input("Enter number1"))
        sub2=int(input("Enter number2"))
        rem=sub1-sub2
        print("The value is",rem)
    elif choice==5:
        loop=0
print("End of the loop")
