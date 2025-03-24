class User:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def describe_user(self):
        print(f"Name:{self.first_name.title()} {self.last_name.title()}")
        print(f"Age:{self.age}")
    def greet_user(self):
        print(f"Hello,{self.first_name.title()}!")
p1=User('aashish','singh negi',19)
p2=User('Caroline','forbes',52)
p1.describe_user()
p1.greet_user()
p2.describe_user()
p2.greet_user()