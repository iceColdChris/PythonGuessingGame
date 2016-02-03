__author__ = 'Chris'
from random import randint

total_games = 1
play_again = True
lowest_guess = 5
lives = 5
total_guesses = 0


def game():

    number = randint(1, 100)
    global total_guesses
    global lives
    global lowest_guess

    while lives > 0:
        guess = raw_input("Please guess a number: ")
        if int(guess) < number:
            print "You guessed to low"
            total_guesses += 1
            lives -= 1
            print "You have " + str(lives) + " lives left"
        elif int(guess) == number:
            print "You guessed correctly"
            total_guesses += 1
            if lowest_guess > total_guesses:
                lowest_guess = total_guesses
            break
        else:
            print "you guessed to high"
            total_guesses += 1
            lives -= 1
            print "You have " + str(lives) + " lives left"

while play_again:
    game()
    again = raw_input("Would you like to play again? (y/n): ")

    if again.lower() == "y":
        play_again = True
        lives = 5
        total_games += 1
    elif again.lower() == "n":
        play_again = False
        average = float(total_guesses/total_guesses)

        print "Your results:"
        print "You played " + str(total_games) + " games."
        print "Your lowest amount of guesses was " + str(lowest_guess)
        print "Your average score was " + str(average)