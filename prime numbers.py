def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
        return True

def find_prime(start,end):
    for num in range(start,end+1):
        if is_prime(num):
            print(num,end=" ")

start=int(input("enter the start range:"))
end=int(input("enter the end range:"))

print(f"prime numbers between {start} and {end} are:")
find_prime(start,end)
