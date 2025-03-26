class User:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attempts=0
    def describe_user(self):
        print(f"Name:{self.first_name.title()} {self.last_name.title()}")
        print(f"Age:{self.age}")
    def greet_user(self):
        print(f"Hello,{self.first_name.title()}!")
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
# instance of class
login1=User('Caroline','forbes',71)
print(f"Number of Logins:{login1.login_attempts}") 
login1.increment_login_attempts()
print(f"Number of Logins:{login1.login_attempts}") 
login1.increment_login_attempts()
print(f"Number of Logins:{login1.login_attempts}") 
login1.reset_login_attempts()
print(f"Logins after Reset:{login1.login_attempts}")