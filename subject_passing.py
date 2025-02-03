# passing a subject
marks1=int(input("Enter your marks: "))
marks2=int(input("Enter your marks: "))
marks3=int(input("Enter your marks: "))
# check for total percentage
a=((marks1+marks2+marks3)/300)
if a >= 0.4 and marks1>=33 and marks2>=33 and marks3>=33:
    print("You are passed.")
else :
    print("You are failed.")  

