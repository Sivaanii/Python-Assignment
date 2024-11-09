def palindrome(s):
    s=s.replace(" ","").lower()

    if s==s[::-1]:
        print(True)
    else:
        print(False)

palindrome(input("enter the string:"))
    
