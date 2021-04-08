import random
import math


def play():
    user = input(
        "What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)


def is_win(player, opponent):
    # return true if the player beats the opponent
    # winning conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False


def play_best_of(n):
    # play against the compute until someone wins best of n games
    # to win, you must win ceil(n/2) games (ie 2/3, 3/5, 4/7)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary or computer_wins < wins_necessary:
        result, user, computer = play()
        if result == 0:
            print("You and the computer have both chosen {}. Its a tie.\n".format(user))
        elif result == 1:
            player_wins += 1
            print("You have chosen {} and computer has chosen {}. You won!\n".format(
                user, computer))
        else:
            computer_wins += 1
            print("You have chosen {} and computer has chosen {}. You lost :(\n".format(
                user, computer))

    if player_wins > computer_wins:
        print("You win! best out of {}".format(n))
    else:
        print("Your lose :( best out of {}".format(n))


if __name__ == '__main__':
    # print(play())
    print(play_best_of(3))
