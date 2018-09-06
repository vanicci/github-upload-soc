# Vanessa Dunford
# Github: https://github.com/vanicci
# Linkedin: https://www.linkedin.com/in/vanessa-dunford-08ab7663/
# Youtube: http://bit.ly/JoinMeOnYouTube
# Twitter: https://twitter.com/vaniccilondon

# Write a program calculating how many seconds old are you?

import time
import sys

def name():
    name = input("What is your name? ")
    while name.isdigit():
        print(name)
        name = input("What is your name? ")
    return name

def user_input():
    while True:
        age = input("What is your age? ")
        try:
            return int(age)
            break
        except ValueError:
            try:
                return float(age)
                break
            except ValueError:
                print("Make sure to enter a real age.")

def again():
    while True:
        again = input("Play again? Yes/No ").lower()
        if again == "no":
            sys.exit(0)
        elif again == "yes":
            break
        else:
            print("That was not an option.")

while True:
    the_name = name()
    age = user_input()
    Days = age * 365
    Hours = Days * 24
    Minutes = Hours * 60
    Seconds = Minutes * 60
    print("Ok {}, I have your results.".format(the_name))
    time.sleep(2)
    print("If you are {} years of age....".format(age))
    time.sleep(2)
    print("You are {} days old.".format(Days))
    time.sleep(2)
    print("You are {} hours old.".format(Hours))
    time.sleep(2)
    print("You are {} minutes old!".format(Minutes))
    time.sleep(2)
    print("You are {} seconds old!".format(Seconds))

    again()
