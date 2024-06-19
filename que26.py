str1=input("Enter a string:")
pre=input("Enter a prefix:")
suff=input("Enter a suffix:")
if str1.startswith(pre):
    print("Starts with the given prefix")
else:
    print("Won't start with the given prefix")   
    
if str1.endswith(suff):
    print("Ends with the given suffix")
else:
    print("Won't end with the given suffix")    

  