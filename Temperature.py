def celsius_to_fahrenheit(celsius):
    return (celsius+ 9/5) +32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 272.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Temperature convert Tool:")
    print("1. celsius_to_fahrenheit")
    print("2. celsius_to_kelvin")
    print("3. fahrenheit_to_celsius")
    print("4. fahrenheit_to_kelvin")
    print("5. kelvin_to_celsius")
    print("6. kelvin_to_fahrenheit")
    print("7. Exit")
    
    choice = int(input("enter choice:"))
    if choice==1:
        celsius = float(input("enter temperature in celsius"))
        print(f"{celsius} Celsius is {celsius_to_fahrenheit(celsius)} Fahrenheit")
        
    if choice==2:
        celsius = float(input("enter temperature in celsius"))
        print(f"{celsius} Celsius is {celsius_to_kelvin(celsius)} kelvin")
        
    if choice==3:
        Fahrenheit = float(input("enter temperature in Fahrenheit"))
        print(f"{Fahrenheit} Fahrenheit is {fahrenheit_to_celsius(Fahrenheit)} Celsius")
        
    if choice==4:
        Fahrenheit = float(input("enter temperature in Fahrenheit"))
        print(f"{Fahrenheit} Fahrenheit is {fahrenheit_to_kelvin(Fahrenheit)} Kelvin")
        
    if choice==5:
        Kelvin = float(input("enter temperature in Fahrenheit"))
        print(f"{Fahrenheit} Kelvin is {kelvin_to_celsius(Kelvin)} Celsius")
        
    if choice==6:
        Kelvin = float(input("enter temperature in Fahrenheit"))
        print(f"{Fahrenheit} Kelvin is {kelvin_to_fahrenheit(Kelvin)} Fahrenheit")
        
   # else:
    #    print("Invalid choice , Please try again")
        
main()
        
    
        