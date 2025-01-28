def get_number():
    return int(input("Enter the number for multiplication table: "))

def get_range():
    start=int(input("Enter the starting range : "))
    end = int(input("Enter the end range : "))
    
    return start,end

def generate_table(number,start,end):
    print(f"\n Multiplication table for {number} from {start} to {end} : \n")
    for i in range(start,end+1):
        print(f"{number}*{i} ={number*i}")
        
def main():
    print("Multiplication table generator")
    number = get_number()
    start,end = get_range()
    generate_table(number,start,end)
    
main()