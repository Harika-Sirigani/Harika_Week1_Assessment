def is_prime(number):
    if number<1:
        return False
    for i in range(2, int(number ** 0.5) +1):
        if number % i ==0:
            return False
    return True

def get_input():
    start = int(input("Enter the start of range : "))
    end = int(input("Enter the end of the range"))
    
    return start,end

def prime_numbers(start,end):
   
    for num in range(start,end):
        if is_prime(num):
            print(num)
    return num   

            
def main():
    start,end = get_input()
    prime_numbers(start,end)
    
main()
   
        
    