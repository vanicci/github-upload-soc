# Vanessa Dunford
# Github: https://github.com/vanicci
# Linkedin: https://www.linkedin.com/in/vanessa-dunford-08ab7663/
# Youtube: http://bit.ly/JoinMeOnYouTube
# Twitter: https://twitter.com/vaniccilondon

# Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.
# Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)

import sys

def firstname():
    firstname = input("What is your first name?: ")
    while firstname.isdigit():
        print(firstname)
        firstname = input("What is your first name?: ")
    return firstname

def midname():
    midname = input("What is your middle name?: ")
    while midname.isdigit():
        print(midname)
        midname = input("What is your middle name?: ")
    return midname

def lastname():
    lastname = input("What is your last name?: ")
    while lastname.isdigit():
        print(lastname)
        lastname = input("What is your last name?: ")
    return lastname

def user_input():
    while True:
        fave_num = input("What is your favourite number?: ")
        try:
            return int(fave_num)
            break
        except ValueError:
            try:
                return float(fave_num)
                break
            except ValueError:
                print("Make sure to enter a number.")

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
	full_name = firstname() + " " + midname() + " " + lastname()
	fave_num = user_input()
	bigger_num = fave_num + 1
	print("Hi {} and welcome to this program!".format(full_name))
	print("If you\'re favourite number is {}.".format(fave_num))
	print("We suggest that {} is a bigger and better number for you. :)".format(bigger_num))

	again()
