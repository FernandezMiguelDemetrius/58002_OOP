def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin * 9/5) - 459.67
    return fahrenheit

temperature = float(input("Enter a temperature: "))
unit = input("Enter the unit of the temperature (F/C/K): ")

if unit == 'F':
    celsius = fahrenheit_to_celsius(temperature)
    kelvin = fahrenheit_to_kelvin(temperature)
    print(f"{temperature} Fahrenheit is equal to {celsius:.2f} Celsius, {kelvin:.2f} Kelvin")
elif unit == 'C':
    fahrenheit = celsius_to_fahrenheit(temperature)
    kelvin = celsius_to_kelvin(temperature)
    print(f"{temperature} Celsius is equal to {fahrenheit:.2f} Fahrenheit, {kelvin:.2f} Kelvin")
elif unit == 'K':
    celsius = kelvin_to_celsius(temperature)
    fahrenheit = kelvin_to_fahrenheit(temperature)
    print(f"{temperature} Kelvin is equal to {celsius:.2f} Celsius, {fahrenheit:.2f} Fahrenheit")
else:
    print("Invalid unit of temperature. Please enter F, C, or K.")
