def atm_simulation():
    balance = 0

    def display_menu():
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
    def check_balance():
        print(f"Your current balance is {balance}")
        
    def deposit():
        nonlocal balance
        amount = int(input("Enter the amount to deposit : "))
        
        if(amount<=0):
            print("Please enter a positive amount")
        else:
            balance += amount
            print(f"Successfully deposited {amount} ")
            print(f" your new balance is {balance}")
        return balance
            
    def withdraw():
        nonlocal balance
        amount = int(input("Enter the amount to withdraw:"))
        if(amount<=0):
            print("Please enter a positive amount")
        elif amount>balance :
            print("Insfficient balanace")
        else:
            balance -= amount
            print("Successfully withdrawn")
            print(f"Your current balance after withdraw is {balance}")
        return balance   
            
    while True:
        display_menu()
        
        choice = int(input("\n Select an option (1-4)"))
        if(choice==1):
            check_balance()
        elif(choice==2):
            deposit()
        elif(choice==3):
            withdraw()
        elif(choice==4):
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    atm_simulation()    
            
    
