# Vanessa Dunford
# Github: https://github.com/vanicci
# Linkedin: https://www.linkedin.com/in/vanessa-dunford-08ab7663/
# Youtube: http://bit.ly/JoinMeOnYouTube
# Twitter: https://twitter.com/vaniccilondon

# “Modern” Roman numerals. Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you had to subtract the smaller one. As a result of this development, you must now suffer. Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.

print("[System] Hi! Enter any number between 1 and 3000 so the program will show you the Modern Roman numeral. In other words, 4 should return 'IV'. Ready?!")

num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

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
