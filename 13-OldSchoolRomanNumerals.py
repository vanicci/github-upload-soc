# Vanessa Dunford
# Github: https://github.com/vanicci
# Linkedin: https://www.linkedin.com/in/vanessa-dunford-08ab7663/
# Youtube: http://bit.ly/JoinMeOnYouTube
# Twitter: https://twitter.com/vaniccilondon

# Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother with any of this new-fangled subtraction “IX” nonsense.
# No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on.

# Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. Make sure to test your method on a bunch of different numbers.

# Hint: Use the integer division and modulus methods.

# For reference, these are the values of the letters used: I = 1 V = 5 X = 10
# L = 50 C = 100 D = 500 M = 1000

print("[System] Hi! Enter any number between 1 and 3000 so the program will show you the Old-school Roman numeral. In other words, 4 should return 'IIII'. Ready?!")

num_map = [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]

num = int(input("Enter any number between 1 and 3000: "))

def int_to_roman(num):
    result = []
    for (arabic, roman) in num_map:
        (factor, num) = divmod(num, arabic)
        result.append(roman * factor)
        if num == 0:
            break
    return "".join(result)

print(int_to_roman(num))
