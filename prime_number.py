n=int(input("Enter the number: "))
for i in range(2,n):
    if n % i==0 :
        print("This Number is not Prime.")
        break
else:
    print("This number is Prime.")