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
# p1=User('aashish','singh negi',19)
class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges=['can add post',
                         'can can delete post','can ban user'
                         'can edit user profile','can change settings']
    def show_privileges(self):
        print(f"Admin Privileges for {self.first_name}: ")
        for privilege in self.privileges:
            print(f"-{privilege}")
admin=Admin('Caroline',"Forbes",56)
admin.describe_user()
admin.show_privileges()