n=int(input("Enter n:"))
num1=0
num2=1
print("Fibonacci series is:",num1,num2,sep=',',end=',')
for i in range(0,n-2):
    num3=num1+num2
    print(num3,end=',')
    num1=num2
    num2=num3