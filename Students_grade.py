def get_input():
    name = input("Enter name: ")
    print("Marks of 5 subjects are:")
    English = int(input("Enter Eng Marks : "))
    Maths = int(input("Enter mat Marks : "))
    Hindi = int(input("Enter hin Marks : "))
    Telugu =int(input("Enter tel Marks : "))
    Social = int(input("Enter soc Marks : "))
    
    return name,English,Maths,Hindi,Telugu,Social

def percentage(English,Maths,Hindi,Telugu,Social):
    Add = English + Maths + Hindi + Telugu + Social
    print(f"Total of all subjects:{Add}")
    Div = (Add/500) * 100
    print(f"Percentage is {Div}")
    if(Div < 40):
        print("Fail")
    else:
        print("Pass")
    return Add,Div

def main():
    name,English,Maths,Hindi,Telugu,Social= get_input()
    
    percentagee = percentage(English,Maths,Hindi,Telugu,Social)
    print(percentagee)
    
main() 

