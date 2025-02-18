def factorial(n) :
    if n==0 or  n==1:
        return 1
    return n*factorial(n-1)

# PERMUTATIONS
n=int(input("Enter the number n: "))
r=int(input("Enter the number r: "))
if r>n:
    print("There is an error.")
else:
    permutations= factorial(n)/factorial(n-r)
    print(f"The Permutation Of the Given numbers is : {permutations}.")

