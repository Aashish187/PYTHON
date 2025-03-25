class Restaurant:
    def __init__(self,name,cuisine):
        self.name=name
        self.cuisine=cuisine
        self.number_served=0
    def describe_restaurant(self):
        print(f"We are {self.name} and we offer {self.cuisine}")
    def open_restaurant(self):
        print(f"{self.name} is open.")
    def set_number_served(self,customers_served):
        self.number_served=customers_served
    def increment_number_served(self,increment):
        self.number_served+=increment
restaurant=Restaurant("Taj",'Thai')
# Printing Numbers of customers served
print(f"We served {restaurant.number_served} customers.")
restaurant.number_served=5 # Updating the value
print(f"We served {restaurant.number_served} customers.")
#Modifying Using a method
restaurant.set_number_served(6)
print(f"We served {restaurant.number_served} customers.")
# Using increment
restaurant.increment_number_served(3)
print(f"We served {restaurant.number_served} customers.")