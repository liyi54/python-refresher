# import random                   # We cover random numbers in the
# rng = random.Random()           #  modules chapter, so peek ahead.
# number = rng.randrange(1, 50) # Get random number between [1 and 50).
#
# guesses = 0
# msg = ""
#
# while True:
#     guess = int(input(msg + "\nGuess my number between 1 and 50: "))
#     guesses += 1
#     if guess > number:
#         msg += str(guess) + " is too high.\n"
#     elif guess < number:
#         msg += str(guess) + " is too low.\n"
#     else:
#         break
#
# input("\n\nGreat, you got it in {0} guesses!\n\n".format(guesses))


# def print_multiples(n, high):
#     for i in range(1, high+1):
#         print(n * i, end="   ")
#     print()
#
# def print_mult_table(high):
#     for i in range(1, high+1):
#         print_multiples(i, i)
#
# print_mult_table(7)


#

# students = [
#     ("John", ["CompSci", "Physics"]),
#     ("Vusi", ["Maths", "CompSci", "Stats"]),
#     ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
#     ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
#     ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]
#
# # Count how many students are taking CompSci
# counter = 0
# for (name, subjects) in students:
#     for s in subjects:                 # A nested loop!
#         if s == "CompSci":
#             counter += 1
#
# print("The number of students taking CompSci is", counter)

import sys
import random
import turtle


def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print(better)   # print the value of better after each iteration
        if abs(approx - better) < 0.000000001:
            return better
        approx = better


def count_odd(list):
    total = 0
    for i in list:
        if i % 2 != 0:
            total += 1
        else:
            continue
    return total


def sum_even(list):
    total = 0
    for i in list:
        if i % 2 == 0:
            total += i
        else:
            continue
    return total


def sum_negative(list):
    total = 0
    for i in list:
        if i < 0:
            total += i
        else:
            continue
    return total


def count_five(list):
    total = 0
    for i in list:
        if len(i) == 5:
            total += 1
        else:
            continue
    return total


def sum_all_but_even(list):
    total = 0
    for i in list:
        if i % 2 == 0:
            even = list.index(i)
            break
        else:
            even = len(list)

    for j in range(even):
        total += list[j]
    return total


def count_all_to_sam(list):
    total = 0
    for name in list:
        if name == "sam" or name == "Sam":
            target = list.index(name) + 1
            break
        else:
            target = len(list)

    for j in range(target):
        total += 1
    return total


def print_triangular_numbers(n):
    values = []
    sum = 0
    for i in range(1, n+1):
        values.append(i)

    for i in values:
        sum += i
        print(str(i) + "\t \t" + str(sum) + "\n")


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            continue
    return True


def num_digits(n):
    count = 0
    while n != 0:
        count = count + 1
        n = n // 10
    return count


def test(did_pass):
    """  Print the result of a test.  """
    line_num = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(line_num)
    else:
        msg = "Test at line {0} FAILED.".format(line_num)
    print(msg)


def test_suite():
    test(count_odd([1, 5, 7, 8, 10, 11, 13]) == 5)
    test(sum_even([1, 2, 3, 4, 5, 6, 7, 8]) == 20)
    test(sum_negative([-1, 3, 5, -3, -10, 6, 8]) == -14)
    test(count_five(["Amaka", "Okiemute", "Sharna", "Rema", "Bantu"]) == 2)
    test(sum_all_but_even([3, 5, 6, 8, 10]) == 8)
    test(sum_all_but_even([1, 3, 5, 7, 9]) == 25)
    test(count_all_to_sam(["Tunde", "Bayo", "Bolanle", "sam", "Chris"]) == 4)
    test(count_all_to_sam(["Tunde", "Bayo", "Bolanle", "Sam", "Chris"]) == 4)
    test(count_all_to_sam(["Tunde", "Bayo", "Bolanle", "John", "Chris"]) == 5)
    print(sqrt(25.0))
    print_triangular_numbers(5)
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))


test_suite()

#   This program draws a shape without going over any edges/path more
#   than once

pirate = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("lightgreen")
pirate.shape("turtle")
pirate.pencolor("blue")

pirate.speed(1)
pirate.setheading(0)

steps = [(0, 70), (90, 50), (45, 50), (90, 50), (45, 50), (125, 85), (145, 70), (145, 85)]

for (turn, move) in steps:
    pirate.left(turn)
    pirate.forward(move)

pirate.hideturtle()

wn.mainloop()

# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1, 2)
    print("Human plays first={0},  winner={1}".format(human_plays_first, result))
    return result


player_wins = 0
comp_wins = 0
draws = 0
i = 0
total_games_played = 0

while True:
    # randomise = random.Random()
    total_games_played += 1
    choices = [True, False]
    # who_plays_first = randomise.choice(choices)
    if i > 1:
        i = 0
    play = play_once(choices[i])
    i += 1

    if play == -1:
        print("You win")
        player_wins += 1
    elif play == 0:
        print("Game drawn")
        draws += 1
    else:
        print("I win")
        comp_wins += 1

    print("You have won {0} rounds \n I have won {1} rounds \n {2} rounds have been drawn".
          format(player_wins, comp_wins, draws))

    percent_wins = round(((player_wins/total_games_played) * 100), 0)

    print("\nYou have won {0} percent of {1} games played".format(percent_wins,total_games_played))

    response = str(input("Do you want to play again? (Yes or No): "))

    if response == "Yes" or response == "yes":
        continue
    else:
        print("Goodbye")
        break
