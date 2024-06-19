num=int(input("Enter a number:"))
sum=0
digit=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print("Sum of the digits of the given number is:",sum)    