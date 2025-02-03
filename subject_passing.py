# passing a subject
sub1=int(input("Enter your marks: "))
sub2=int(input("Enter your marks: "))
sub3=int(input("Enter your marks: "))
# check for total percentage
total_percentage=((sub1+sub2+sub3)/300)*100
if total_percentage >= 40 and sub1>=33 and sub2>=33 and sub3>=33:
    print("You are passed.")
else :
    print("You are failed.")  

