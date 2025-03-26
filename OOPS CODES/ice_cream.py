class Restaurant:
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine
    def describe_restaurant(self):
        print(f"We are {self.name} and we offer {self.cuisine}")
    def open_restaurant(self):
        print(f"{self.name} is open.")
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine,flavours):
        super().__init__(name, cuisine)
        self.flavours=flavours
    def display_flavours(self):
        print(f"We have these ice-cream flavours available.")
        for i in self.flavours:
            print(i)
f1=IceCreamStand("Taj",'Thai',['mango','chocolate','strawberry'])
f1.display_flavours()