n=int(input("Enter the number: "))
product=1
for i in range(1,n+1):
    product=product*i
print(f"Factorial of {n} is {product}.")

#   BY USING FUNCTIONS
def factorial(n):
    if n==1 or n==0:
     return 1
    return n *factorial (n-1)
n=int(input("Enter the number: "))
print(f"The Factorial of this number is : {factorial(n)}")
