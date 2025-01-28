import random

def number_guessing_game():
    print("Welcome to guessing game")
    print("I'm thinking of a number between 1 and 100")
    
    target_number = random.randint(1,100)
    #print(target_number)
    
    attempts = 0
    
    while True:
        
        guess = int(input("Enter your guess : "))
        attempts += 1
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {target_number} in {attempts} attempts.")
            break
        
def main():
    print(number_guessing_game())
    
main()
        