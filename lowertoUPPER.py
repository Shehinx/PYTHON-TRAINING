inputString = input("Enter the string:")
out=''
for i in inputString:
    if i.isupper():
        o=i.lower()
    elif i.islower():
        o=i.upper()
    else:
        o=i
    outputstring += o
print(outputstring)
