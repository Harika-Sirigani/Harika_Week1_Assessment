def strength(password):
    lower =0
    upper =0
    digit=0
    length = len(password)
    special =0
    for c in password:
        if c.islower():
            lower = 1
        elif c.isupper():
            upper = 1
        elif c.isdigit():
            digit=1
        else:
            special = 1
            
    return lower ==1 and upper == 1 and digit ==1 and length >=8 and special ==1

def main():
    password = input("enter password : ")
    if strength(password):
        print("password is strong ")
    else:
        print("password is weak")
        
main()