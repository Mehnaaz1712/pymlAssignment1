str1=input("Enter a string:")
punctuation=".,?!:;'{}[]()-_\"..."
for i in str1:
    if i in punctuation:
        str2=str1.replace(i,"")
print("String without punctuation is:",str2)        