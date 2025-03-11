import art
import random
from game_data import data

def compare_users_followers(u_a, u_b):
    """
    Compares the follower count of two users
    :param u_a:
    :param u_b:
    :return: dict
    """
    if u_a['follower_count'] > u_b['follower_count']:
        return {
            'answer': 'a',
            'user_data': u_a
        }
    else:
        return {
            'answer': 'b',
            'user_data': u_b
        }

def choice_excluded(excluded_index):
    """
    Chooses a random user from the data list excluding the user at the excluded_index
    :param excluded_index:
    :return:
    """
    user = random.choice(data)
    while data.index(user) == excluded_index:
        user = random.choice(data)
    return user

def format_user_data(user_data):
    """
    Formats the user data into a string
    :param user_data:
    :return: str
    """
    return f"{user_data['name']}, a {user_data['description']} from {user_data['country']}"


def print_users_data(u_a , u_b):
    """
    Prints the user data
    :param u_a:
    :param u_b:
    :return:
    """
    print(f"Compare A: {format_user_data(u_a)}")
    print(art.vs)
    print(f"Against B: {format_user_data(u_b)}")


def clear_screen():
   """
    Clears the screen
    :return:
   """
   print('\n' * 100)
   print(art.logo)


def game():
    """
    The main game function
    :return:
    """
    print(art.logo)

    user_on_streak = True
    score = 0
    user_a = None
    while user_on_streak:
        if user_a is None:
            user_a = random.choice(data)

        user_a_index = data.index(user_a)
        user_b = choice_excluded(user_a_index)
        correct_answer = compare_users_followers(user_a,user_b)

        print_users_data(user_a,user_b)
        player_input = input(f"Who has more followers? Type 'A' or 'B': ").lower()

        if player_input == correct_answer['answer']:
            clear_screen()
            print("Correct!")
            score += 1
            user_a = correct_answer['user_data']
            user_on_streak = True
        else:
            clear_screen()
            print(f"Sorry, that's wrong. Final score: {score}")
            user_on_streak = False


game()




