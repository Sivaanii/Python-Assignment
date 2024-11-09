n=int(input("enter the number of terms:"))
a,b=0,1
for i in range(n):
    if i<n-1:
        print(a,end=",")
    else:
        print(a)
    a,b=b,a+b

    
    
