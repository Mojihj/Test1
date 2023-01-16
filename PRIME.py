# Taeen adad aval
n= int (input("Please Enter Your Number:"))
def is_prime (n):
    aval=True
    for i in range(2,n):
        if n % i ==0:
            aval=False
    return aval
if is_prime (n)==True:
    print ("The number is prime")
else:
     print ("The number is NOT prime")



    


