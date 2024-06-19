num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
op=input("Enter an operator (+,-,*,/):")
if op=='+':
    print("Sum is:",num1+num2)
elif op=='-':
    print("Difference is:",num1-num2)    
elif op=='*':
    print("Multiplication is:",num1*num2)    
elif op=='/':
    if num2!=0:
        print("Division is:",num1/num2)    
    else:
        print("Division not defined")  
else:
    print("Invalid operator")    
