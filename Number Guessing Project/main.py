from art import logo
import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid input.")
        set_difficulty()

def generate_number(lowest_point = 1 , highest_point = 100):
    print(f"Welcome! A number between {lowest_point} and {highest_point} has been generated.")
    return random.randint(lowest_point,highest_point)

def get_user_guess():
    user_guess = int(input("Make a guess: "))
    return user_guess

def compare_guesses(user_guess, number):
    if user_guess == number:
        print("You got it!")
        return True
    elif user_guess > number:
        print("Too high.")
        return False
    elif user_guess < number:
        print("Too low.")
        return False


def game():
    print(logo)
    user_attempts = set_difficulty()
    number = generate_number(1,50)
    def process_user_guess(user_attempts_amount):
        print(f"You have {user_attempts_amount} attempts remaining.")
        user_guess = get_user_guess()
        if user_attempts_amount == 0:
            print("You've run out of guesses. You lose.")
            return
        else:
            if compare_guesses(user_guess, number):
                return
            else:
                user_attempts_amount -=1
                process_user_guess(user_attempts_amount)

    process_user_guess(user_attempts)


game()




