print("1.Convert Celsius to fahrenheit")
print("2.Convert fahrenheit to celsius")
choice=int(input("Choose 1 or 2:"))
if choice==1:
    cel=int(input("Enter the temperature in celcius:"))
    fah=((9/5)*cel)+32
    print("Temperature in fahrenheit is:",fah)
elif choice==2:
    fah=int(input("Enter temperature in fahrenheit:"))
    cel=(5/9)*(fah-32)    
    print("Temperature in celsius is:",cel)
else:
    print("Invalid choice")    