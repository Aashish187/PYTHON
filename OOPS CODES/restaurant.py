class Restaurant:
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine
    def describe_restaurant(self):
        print(f"We are {self.name} and we offer {self.cuisine}")
    def open_restaurant(self):
        print(f"{self.name} is open.")
restaurant=Restaurant("Taj",'Thai')
print(f"Restaurant name is {restaurant.name}")
print(f"Cuisine type is {restaurant.cuisine}")
restaurant.describe_restaurant()
restaurant.open_restaurant()