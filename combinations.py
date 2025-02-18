def factorial(n) :
    if n==0 or  n==1:
        return 1
    return n*factorial(n-1)

# COMBINATIONS
n=int(input("Enter the number n: "))
r=int(input("Enter the number r: "))
if r>n:
    print("There is an error.")
else:
    combination= factorial(n)/(factorial(n-r)*factorial(r))
    print(f"The Combination Of the Given numbers is : {combination}.")

