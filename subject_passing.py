# passing a subject
sub1=int(input("Enter your marks: "))
sub2=int(input("Enter your marks: "))
sub3=int(input("Enter your marks: "))
# check for total percentage
a=((sub1+sub2+sub3)/300)
if a >= 0.4 and sub1>=33 and sub2>=33 and sub3>=33:
    print("You are passed.")
else :
    print("You are failed.")  

