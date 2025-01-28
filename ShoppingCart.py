def shoppingCart():
    cart={}
    
    print("1. add \n 2. view \n 3. Total \n 4. Exit \n")
    
    while True:
        choice = input("Enter your choice : ")
        if choice == "add":
            item=input("Enter the item name :")
            price = float(input("enter the price : "))
            cart[item] = price
            
            
        if choice == "view":
            print(" \n your cart ")
            for item, price in cart.items():
                print(f"{item}: {price}")
        
        if choice == "total":
            total = sum(cart.values())
            print(f"\n Total price : {total}")
            
        if choice == "exit":
            print("\n exiting the shopping cart .....")
            break
if __name__=="__main__":
    shoppingCart()