def get_input():
    number = int(input("Enter num : "))
    
    return  number

def factorial(number):
    if (number < 1):
        print("Negative numbers are not allowed")
    fact = 1
    for i in range(1,number+1):
        fact *= i
    
    print(f"factorial of {number} is {fact}")
        
    return fact

def main():
    number = get_input()
    value = factorial(number)
    #if(number>1):
    print(value)
    
main()