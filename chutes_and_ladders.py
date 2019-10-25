from random import randint
import statistics
from matplotlib import pyplot as plt


def make_move(connections, current_space):
    """Returns new_space after moving from current_space on board given by connections"""
    die_roll = randint(1,6)
    new_space = connections.get(current_space + die_roll, current_space + die_roll)
    return new_space if new_space <= 100 else current_space


def simulate_game(connections):
    """Returns number of turns required to complete one game with board given by connections"""
    space = 0
    num_of_turns = 0
    while space != 100:
        num_of_turns += 1
        space = make_move(connections, space)
    return num_of_turns


def user_input_positive_int():
    "Returns a positive integer as input by user."
    valid_input = False
    while not valid_input:
        try:
            number_of_games = int(input("How many games to simulate? "))
            if number_of_games <= 0:
                raise Exception
        except Exception:
            print("Please enter a positive integer!")
        else:
            valid_input = True
    return number_of_games


board_connections = {1:38, 4:14, 9:31, 16:6, 21:42, 
28:84, 36:44, 47:26, 49:11, 51:67, 56:53, 62:19,
64:60, 71:91, 80:100, 87:24, 93:73, 95:75, 98:78}


number_of_games = user_input_positive_int()
my_list = [simulate_game(board_connections) for i in range(number_of_games)]

print(f"Mean number of turns = {statistics.mean(my_list)}.")
print(f"Median number of turns = {statistics.median(my_list)}.")
print(f"Max number of turns = {max(my_list)}.")
print(f"Min number of turns = {min(my_list)}.")

binwidth = 5
plt.hist(my_list, bins=[1+binwidth*i for i in range(200 // binwidth)], density=True)
plt.show()

print("some changes")