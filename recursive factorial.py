def factorial(n):
    if n==1 or n==0:
        return 1
    else:
      return n*factorial(n-1)

num=int(input("enter the number to find the the factorial:"))
result=factorial(num)
print("factorial of the number" ,num ,"is" ,result)
