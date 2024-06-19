str1=input("Enter 1st string:")
str2=input("Enter 2nd string:")
count=0
if len(str1)==len(str2):
    for i in str1:
        if i in str2:
            count=count+1
    if count==len(str1):
        print("strings are anagrams of each other")
else:
    print("not anagrams")