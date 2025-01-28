def get_input():
    word = input("enter a word:")
    return word 

def palindrome(word):
    rev_word = word[::-1]
    if word == rev_word:
        return "palindrome"
    else:
        return "Not a palindrome"
    
def main():
    word = get_input()
    print(palindrome(word))
    
main()
