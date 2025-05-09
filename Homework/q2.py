#Prime Number
num=int(input("Enter a Number"))

def check_prime(n):
    if n<=1:
        return False
    if n==2 or n==3 or n==5:
        return True
    for i in range(2,int(n/2)):
        if n%i==0:
            return False
        else:
            return True
    
if check_prime(num)==True:
    print("The number is prime")
else:
    print("The Number is not prime")
