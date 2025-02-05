def conversion(temp_in_c):
    temp_in_c=float(input("Enter the Temperature in °C: "))
    fahrenheit_temp= (temp_in_c*(9/5))+32
    print(f"Temperature in Fahrenheit is: {round(fahrenheit_temp,2)} °F")
conversion(34)