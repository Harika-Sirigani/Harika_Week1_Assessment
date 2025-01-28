

def secondlar(num):
    num.sort(reverse = True)
    return num[1]

if __name__ == "__main__":
    num = list(map(int,input("enter num").split()))
    print(secondlar(num))
    
