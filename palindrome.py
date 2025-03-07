n=int(input())
reverse=int(str(n)[::-1])
if(n<0):
    print("The number is not palindrome")
if(n==reverse):
    print("The number is a palindrome")
else:
    print("The number is not palindrome")
